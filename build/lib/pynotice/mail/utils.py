from zmail import server
from typing import Optional


class SMTPConfigException(Exception):
    def __init__(self):
        err = "SMTP Server Configuration Exception\n please confirm your parameters are correct"
        Exception.__init__(self, err)


def config_server(sender_email:str, sender_autorization_code:str, smtp_host: Optional[str] = None, smtp_port: Optional[int] = None, timeout=10):
    """
    smtp server configuration

    :param sender_email: sender's email
    :param sender_autorization_code:  sender's smtp authorization code
    :param smtp_host: smtp host address
    :param smtp_port: smtp host port
    :param timeout: timeout
    :return: smtp server object
    """
    assert isinstance(sender_email, str), "sender_email should be given a string"
    assert isinstance(sender_autorization_code, str), "sender_authorization_code should be given a string"

    s = server(sender_email, sender_autorization_code, smtp_host=smtp_host, smtp_port=smtp_port, timeout=timeout)
    if s.smtp_able():
        print("server config success")
        return s
    else:
        raise SMTPConfigException



