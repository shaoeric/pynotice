#-*- coding : utf-8 -*-
# coding: utf-8

from pyprompt.sound.utils import *


def promptOnfinish(filepath=success_audio):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            check_file_type(filepath)
            result = fun(*args, **kwargs)
            play(filepath)
            return result
        return wrapper
    return decorator



