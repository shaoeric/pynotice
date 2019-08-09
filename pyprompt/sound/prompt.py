#-*- coding : utf-8 -*-
# coding: utf-8

from pyprompt.sound.utils import *


def promptOnfinish(filepath=success_audio):
    """
    decorator function, when the fun finishes, promptOnfinish() will play an audio in wav format(default is success_audio)

    :param filepath: wav audio path
    :return:
    """
    def decorator(fun):
        def wrapper(*args, **kwargs):
            check_file_type(filepath)
            result = fun(*args, **kwargs)
            play(filepath)
            return result
        return wrapper
    return decorator


def promptOnException(filepath=error_audio):
    """
    decorator function, when fun goes wrong or raises Exception, promptOnException() will play an audio in wav format(default is error_audio)

    :param filepath: wav audio path
    :return:
    """
    def decorator(fun):
        def wrapper(*args, **kwargs):
            check_file_type(filepath)
            try:
                result = fun(*args, **kwargs)
                return result
            except Exception as e:
                play(filepath)
                raise e
        return wrapper
    return decorator

