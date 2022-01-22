import glob
import os
import time

from .audio_utils import join_wav_files
from .constants import BACKTRACK_RECORDINGS_DIR, logger


def get_wav_file_name(start_time: int, end_time: int):
    start_time_str = time.strftime('%H:%M', time.localtime(start_time))
    end_time_str = time.strftime('%H:%M', time.localtime(start_time))
    return f'{start_time_str}-{end_time_str}.wav'


def rewind_audio(minutes: int):
    seconds = minutes * 60
    list_of_files = glob.glob(os.path.join(BACKTRACK_RECORDINGS_DIR, "*.wav"))
    current_time = time.time()
    start_time = int(current_time - seconds)
    start_times = [int(el.split("/")[-1].replace(".wav", "")) for el in list_of_files]
    sorted_start_times = list(sorted(start_times))
    wav_out_file = os.path.join(
        os.path.expanduser("~"),
        get_wav_file_name(start_time, int(current_time))
    )
    join_wav_files(
        [
            os.path.join(BACKTRACK_RECORDINGS_DIR, f"{st}.wav")
            for st in sorted_start_times
            if st > (start_time - 10)
        ],
        wav_out_file,
    )
    logger.info(f"rewind-ed and stored at {wav_out_file}")
