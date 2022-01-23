import logging
import os.path

import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

REWINDER_RECORDINGS_DIR = os.path.join(os.path.expanduser("~"), ".rewinder_recordings")

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(message)s",
    level=logging.INFO,
    filename=os.path.join(os.path.expanduser("~"), ".rewinder.logs"),
    filemode="a",
)
