from multiprocessing import Process

import typer

from .rewind import rewind_audio
from .cleanup import schedule_cleanup
from .daemon import initiate_daemon

app = typer.Typer()


@app.command()
def daemon():
    initiate_daemon_process = Process(target=initiate_daemon, args=())
    initiate_cleanup_process = Process(target=schedule_cleanup, args=())
    initiate_daemon_process.start()
    initiate_cleanup_process.start()
    initiate_daemon_process.join()
    initiate_cleanup_process.join()


@app.command()
def rewind(minutes_to_backtrack: int):
    rewind_audio(minutes_to_backtrack)
