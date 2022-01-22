import os
import time

import pyaudio

from .audio_utils import write_wav_file
from .constants import CHUNK, RATE, BACKTRACK_RECORDINGS_DIR, FORMAT, CHANNELS, logger


def capture_wav_frames(p, stream, seconds_to_capture: int = 10):
    start_timestamp = time.time()
    try:
        wav_frames = [stream.read(CHUNK) for i in range(0, int(RATE / CHUNK * seconds_to_capture))]
        write_wav_file(
            p,
            wav_frames,
            os.path.join(
                BACKTRACK_RECORDINGS_DIR,
                f'{int(start_timestamp)}.wav'
            )
        )
    except KeyboardInterrupt:
        stream.stop_stream()
        stream.close()
        p.terminate()
        exit(0)


def initiate_daemon():
    logger.info('initiating recording')
    if not os.path.exists(BACKTRACK_RECORDINGS_DIR):
        os.mkdir(BACKTRACK_RECORDINGS_DIR)
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    while True:
        capture_wav_frames(p, stream)
