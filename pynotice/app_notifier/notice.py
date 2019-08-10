#-*- coding : utf-8 -*-
# coding: utf-8

import subprocess

def _notifier(msg):
    return subprocess.call(["notifier", "notify", "--msg", msg ])


def noticeOnFinish(filepath=success_audio):
    """
    decorator function, when the func finishes, noticeOnFinish() will invoke
    `notifier <https://metacpan.org/pod/distribution/App-Notifier-Client/bin/notifier>`_.

    :param filepath: wav audio path
    :return:
    """
    def decorator(fun):
        def wrapper(*args, **kwargs):
            result = fun(*args, **kwargs)
            _notifier("The function completed")
            return result
        return wrapper
    return decorator


def noticeOnException(filepath=error_audio):
    """
    decorator function, when the func goes wrong or raises an Exception, noticeOnException() will invoke
    `notifier <https://metacpan.org/pod/distribution/App-Notifier-Client/bin/notifier>`_.

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
                _notifier("The function raised an exception")
                raise e
        return wrapper
    return decorator

