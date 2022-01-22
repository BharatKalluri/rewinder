import logging
import os
import wave
from typing import List

import pyaudio

from .constants import CHANNELS, FORMAT, RATE, logger


def write_wav_file(
    py_audio_instance: pyaudio.PyAudio, wav_frames: List, file_name: str
):
    wf = wave.open(file_name, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(py_audio_instance.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(wav_frames))
    wf.close()
    logger.info(f"saved {file_name}")


def join_wav_files(in_files: list, out_file_path: os.path):
    data = []
    for infile in in_files:
        w = wave.open(infile, "rb")
        data.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()
    output = wave.open(out_file_path, "wb")
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()
