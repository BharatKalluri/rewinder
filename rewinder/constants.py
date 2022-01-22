import logging
import os.path

import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

BACKTRACK_RECORDINGS_DIR = os.path.join(
    os.path.expanduser("~"), ".backtrack_recordings"
)

logger = logging.getLogger(__name__)
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
