from filetype import guess
from pynotice.sound import *
import simpleaudio as sa


class FileIsNotWavFormatException(Exception):
    def __init__(self, filepath):
        self.filepath = filepath
        err = "{} is not in WAV format".format(self.filepath)
        Exception.__init__(self, err)


def check_file_type(filepath):
    filetype = guess(filepath).extension
    if filetype == "wav":
        return True
    else:
        raise FileIsNotWavFormatException(filepath)


def play(filepath=success_audio):
    wave_obj = sa.WaveObject.from_wave_file(filepath)
    play_obj = wave_obj.play()
    play_obj.wait_done()
