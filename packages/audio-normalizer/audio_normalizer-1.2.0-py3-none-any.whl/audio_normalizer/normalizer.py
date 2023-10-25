"""
This is a normalizer for mp3 and wav files. Its a final project for Havard CS50P.

The approach in this program to normalize audio differs in comparison to most other programs that implement this task. 
Most normalizers amplify an audio signal until the highest transient reaches 0 dB.
The downside of this approach is that the audio signal can only be amplified based on a single maximum transient. 
In other words, the whole normalizing process depends on one transient, which is inefficient.

This program, however, doesn't depend on a single transient. 
It rather splits the original signal into four separate signals (left positive, left negative, right positive, and right negative). 
Then it uses an algorithm that finds several transients that exceed a calculated value based on the audio file's duration and actual volume. 
For each split signal, a copy is being created, a dummy signal. In the dummy signals, the found transients are turned into the value of zero. 
The next task is to find the new maximum transient in each modified dummy signal like any other simple normalizer. 
The new maximum value is then saved for the final amplification.

At this stage, the program finds all amplitudes in the original split signals where the previously found transients are sitting. 
The split audio signals are then amplified based on the new maximum transient. 
All amplitudes that exceed (clip) above 0 dB are lowered to 0 dB without manipulating the original signal except for the volume.
Finally, all the amplified split signals are merged together and are saved as the original file name and type. 
All the ID3 tags, including the album cover, are also maintained in the new normalized file.

As a result, the user gets an audiofile normalized to 0 dB without losing noticeable dynamic range or the overall audio quality.
"""


import os
import numpy as np
from .utils import ProgressHandler, ArrayModifiers, File, Plot


class Normalizer:
    @staticmethod
    def get_data_type(sample_width: int) -> np.dtype:
        """
        Gets the data type for all the arrays, based on the origin signal data type.
        Sample width 1 == 1 byte == 8 bit == int8,...
        """
        return {1: np.int8, 2: np.int16, 4: np.int32}[sample_width]
    
    @staticmethod
    def get_max_value(sample_width: int) -> int:
        """
        (int(((1 << bits) - 1) / 2)
        Maximum value that can be represented given the sample width
        """
        return {1: 127, 2: 32767, 4: 2147483647}[sample_width]
        
    @staticmethod
    def find_transient_threshold(signal_array: np.ndarray, frame_rate: int) -> int:
        """
        Calculate a transient threshold based on the maximum values in equal-sized frames of a signal array.
        """
        # TODO Find better algorithm
        blocks_max = []
        global_max = signal_array.max()
        
        for i in range(0, signal_array.size, frame_rate):
            block = signal_array[i : i + frame_rate]
            blocks_max.append(int(block.max()))
            threshold = int(sum(blocks_max) / len(blocks_max))
            
        threshold - (global_max - threshold)
            
        filtered_list = [x for x in blocks_max if x >= threshold]
        threshold = int(sum(filtered_list) / len(filtered_list))   
         
        return threshold

    @staticmethod
    def find_transients(signal_array: np.ndarray, threshold: int) -> np.ndarray:
        """
        Find the indices where the signal array values exceed a given threshold.
        """
        return np.where(signal_array >= threshold)[0]

    @staticmethod
    def find_amplitudes(signal_array: np.ndarray, transients: np.ndarray) -> list[list[int]]:
        """
        Determine amplitudes within a signal array given specific transients.
        """
        
        # Find beginning and ending of the amplitudes in wich the transients are sitting
        indices_of_ones = np.where(signal_array == 1)[0]
        all_indices = np.searchsorted(indices_of_ones, transients)
        
        amplitudes = []
        
        # Go through all indices and find the amplitudes while checking the boundaries
        for idx in all_indices:
            before_index = idx - 1
            after_index = idx

            # Check the lower boundary
            if before_index < 0:
                start_idx = 0
            else:
                start_idx = indices_of_ones[before_index]

            # Check the upper boundary
            if after_index >= len(indices_of_ones):
                end_idx = len(indices_of_ones)
            else:
                end_idx = indices_of_ones[after_index]
            
            amplitudes.append([start_idx, end_idx])

        return amplitudes

    @staticmethod
    def find_amplification_factor(signal_array: np.ndarray, amplitudes: list, max_value: int) -> float:
        """
        Find a factor to amplify a signal array while considering designated amplitude regions.
        """
        masked_signal_array = signal_array.copy()

        for start, end in amplitudes:
            masked_signal_array[start:end] = 0

        amplification_factor = np.float32(
            max_value / np.max(masked_signal_array)
        )
        
        if amplification_factor < 1:
            amplification_factor = 1.0
        
        return amplification_factor

    @staticmethod
    @ProgressHandler.update_bar
    def amplify(
        signal_array: np.ndarray, amplification_factor: float, amplitudes: list[list], max_value: int
    ) -> None:
        """
        Amplify a signal array while considering designated amplitude regions and an amplification factor.
        """
        AUDIO_START = 0
        AUDIO_END = len(signal_array)
        FIRST_AMP = amplitudes[0][0]
        LAST_AMP = amplitudes[-1][1]

        def amplify_segment(start: int, end: int, factor: float) -> None:
             # Convert to float for precision during amplification
            segment = signal_array[start:end].astype(float)
            # Identify where the signal is above the threshold
            above_threshold = segment > 3
            # Amplify only where the signal is above the threshold
            segment[above_threshold] *= factor  
            # Clip to maintain within the valid range, considering the original data type
            np.clip(segment, -max_value, max_value, out=segment)
            # Rounding and type conversion: rounding is done post-clipping to ensure to stay within limits
            signal_array[start:end] = np.round(segment).astype(signal_array.dtype)
            
        if AUDIO_START != FIRST_AMP:
            amplify_segment(AUDIO_START, FIRST_AMP, amplification_factor)

        for i, (start, end) in enumerate(amplitudes):
            if start == end:
                continue

            # Calculate the adjusted amplification factor to avoid overflow
            segment_max = np.max(np.abs(signal_array[start:end]))  # Find the max value in the current segment
            if segment_max * amplification_factor > max_value:
                factor = max_value / segment_max
            else:
                factor = amplification_factor

            amplify_segment(start, end, factor)

            # Handling the segments between the specified amplitudes
            if i + 1 < len(amplitudes):
                next_start = amplitudes[i + 1][0]
                amplify_segment(end, next_start, amplification_factor)

        if LAST_AMP != AUDIO_END:
            amplify_segment(LAST_AMP, AUDIO_END, amplification_factor)

    @staticmethod
    def check_for_clipping(signal_array: np.ndarray, max_value: int) -> None:
        """
        Adjusts the signal array values to ensure they do not exceed the maximum allowed volume.
        """
        signal_array[signal_array > max_value] = max_value
    
    @staticmethod
    @ProgressHandler.update_bar
    def prepare_signal(signal_array: np.ndarray, channels: int, data_type: np.dtype, max_value: int) -> list[np.ndarray]:
        """
        Prepare original signal array for the normalizing process.
        """
        EQUAL_VALUES = [1, -1]
        REPLACE_VALUES = [0, 0]

        ArrayModifiers.replace_equals_with_values(
            signal_array, EQUAL_VALUES, REPLACE_VALUES
        )
        signal_arrays = ArrayModifiers.split_audio_array(signal_array, channels, data_type)
        
        # 1s are placeholders to know where positive or negative values have been
        # It keeps all the samples in original order
        # The original length is also maintained
        # All arrays are processed unsigned. Array "left negative" for example contains only unsigned values. 
        # The negative arrays will be converted back to negative values after normalizing.
        for i in range(0, len(signal_arrays), 2):
            ArrayModifiers.replace_negatives_with_value(signal_arrays, [i], 1)
            ArrayModifiers.replace_positives_with_value(signal_arrays, [i + 1], -1)
            ArrayModifiers.negative_to_positive(signal_arrays, [i + 1], max_value)
            
        return signal_arrays

    @staticmethod
    @ProgressHandler.update_bar
    def undo_prepare_signal(signal_arrays: list[np.ndarray], channels: int, data_type: np.dtype) -> np.ndarray:
        """
        Convert the prepared signal arrays back to the original structure
        """
        DELETE_VALUES = [1, -1]
        
        for i in range(0, len(signal_arrays), 2):
            ArrayModifiers.positive_to_negative(signal_arrays, [i + 1])
            
        signals_left_right = ArrayModifiers.merge_split_arrays(signal_arrays, channels, data_type)
        signals_left_right = ArrayModifiers.delete_values(signals_left_right, DELETE_VALUES)
        
        if channels == 2:  # STEREO
            return ArrayModifiers.combine_arrays(signals_left_right)
        
        return signals_left_right[0].reshape(-1, 1) # MONO


@ProgressHandler.update_bar
def normalize_signal(signal_array: any, channels: int, frame_rate: int, sample_width: int) -> np.ndarray:
    
    data_type = Normalizer.get_data_type(sample_width)
    max_value = Normalizer.get_max_value(sample_width)
    
    signal_array = ArrayModifiers.array_to_numpy_array(signal_array, data_type)
    signal_array = ArrayModifiers.reshape_to_channels(signal_array, channels)
    
    signal_arrays = Normalizer.prepare_signal(signal_array, channels, data_type, max_value)
    
    for signal_array in signal_arrays:
        threshold = Normalizer.find_transient_threshold(
            signal_array, frame_rate
        )
        #Plot.plot_find_transient_threshold(signal_array, threshold)
        transients = Normalizer.find_transients(signal_array, threshold)
        
        # Removes transients that are directly next to each other. 
        # Its only important to know one transient per amplitude that exceeded the threshold
        transients = ArrayModifiers.remove_adjacent_by_difference(transients)
        
        if amplitudes := Normalizer.find_amplitudes(signal_array, transients):
            amplification_factor = Normalizer.find_amplification_factor(
                signal_array, amplitudes, max_value
            )
            
            # Nothing to amplify
            if amplification_factor == 1.0:
                continue
            try:
                Normalizer.amplify(signal_array, amplification_factor, amplitudes, max_value)
            except:
                print("Amplification error")
                continue
            
            Normalizer.check_for_clipping(signal_array, max_value)

    normalized_signal = Normalizer.undo_prepare_signal(signal_arrays, channels, data_type)
    return normalized_signal


progress = ProgressHandler()


def normalize_file(file: str, folder: str, format: str) -> None:
    File.check_folder(folder)
    
    if audio_file_data := File.open_audio(file, folder):
        progress.current_file = audio_file_data["filename"]
        normalized_signal = normalize_signal(
            audio_file_data["signal_array"],
            audio_file_data["channels"],
            audio_file_data["frame_rate"],
            audio_file_data["sample_width"]
        )
        
        File.save_as(normalized_signal, audio_file_data, folder, format)
        File.write_tags(file, folder, format)
        
        
def normalize_folder(folder) -> None:
    progress.running = True
    done_files = File.check_folder(folder)
    
    try:
        os.listdir(f"{folder}")
    except FileNotFoundError:
        progress.reset()
        return 1

    for file in os.listdir(f"{folder}"):
        file_name, _ = os.path.splitext(file)
        
        if progress.terminate:
            progress.reset()
            return None
        
        if file_name not in done_files:
            normalize_file(file, folder, progress._format)
                
        progress.bar = 0
        
    progress.reset()
    return None


if __name__ == "__main__":
    normalize_folder("./")
