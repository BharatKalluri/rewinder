import glob
import logging
import os
import time

from .constants import BACKTRACK_RECORDINGS_DIR, logger


def initiate_cleanup(retain_recordings_till_minutes: int, run_cleanup_every_x_min: int):
    logger.info(f"initiating cleanup")
    logger.info(f"retaining recording till {retain_recordings_till_minutes} min")
    logger.info(f"running cleanup evey {run_cleanup_every_x_min} min")

    current_time = int(time.time())
    retain_recordings_till = current_time - (retain_recordings_till_minutes * 60)
    list_of_files = glob.glob(os.path.join(BACKTRACK_RECORDINGS_DIR, "*.wav"))
    start_times = list(
        sorted(int(el.split("/")[-1].replace(".wav", "")) for el in list_of_files)
    )
    files_to_delete = [
        os.path.join(BACKTRACK_RECORDINGS_DIR, f"{ts}.wav")
        for ts in start_times
        if ts < retain_recordings_till
    ]
    logger.info(f"deleting files: {files_to_delete}")
    [os.remove(f) for f in files_to_delete]
    time.sleep(run_cleanup_every_x_min * 60)


def schedule_cleanup(
    retain_recordings_till_minutes: int = 60, run_cleanup_every_x_min: int = 30
):
    while True:
        initiate_cleanup(retain_recordings_till_minutes, run_cleanup_every_x_min)
