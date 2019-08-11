#-*- coding : utf-8 -*-
# coding: utf-8

from pynotice.sound.utils import *


def noticeOnFinish(filepath=success_audio):
    """
    decorator function, when the fun finishes, noticeOnfinish() will play an audio in wav format(default is success_audio)

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


def noticeOnException(filepath=error_audio):
    """
    decorator function, when fun goes wrong or raises Exception, noticeOnException() will play an audio in wav format(default is error_audio)

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

