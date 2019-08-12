from pynotice.mail.utils import *


def noticeOnFinish(sender_email, sender_authorization_code, receiver_email, mail_subject="Finish!", mail_content="", attachments=None, smtp_host=None, smtp_port=None):
    """
    When the decorated function finishes, noticeOnfinish() will send an email with the result of the function and attachments to receiver's email if the stmp of the sender's email is available.

    :param sender_email: sender's email
    :param sender_authorization_code:  sender's smtp authorization code
    :param receiver_email: receiver's email or a list of emails
    :param mail_subject: subject of the email
    :param mail_content: content of the email
    :param attachments: attachments available
    :param smtp_host: smtp host address
    :param smtp_port: smtp host port
    :return: smtp server object
    """
    assert isinstance(mail_subject, str), "mail_subject should be given a string or ''"
    assert isinstance(receiver_email, str) or isinstance(receiver_email, list), "receiver_email should be given a string or a list"

    def decorator(fun):
        def wrapper(*args, **kwargs):
            s = config_server(sender_email, sender_authorization_code, smtp_host, smtp_port)
            result = fun(*args, **kwargs)
            mail = {
                'subject': mail_subject,
                'content_text': mail_content + "\n" + str(result),
                'attachments': attachments
            }
            print("sending email...")
            s.send_mail(receiver_email, mail)
            return result
        return wrapper
    return decorator


def noticeOnException(sender_email, sender_authorization_code, receiver_email, mail_subject="Exception!", mail_content="", smtp_host=None, smtp_port=None):
    """
    When the decorated function goes wrong, noticeOnException() will send an email with the Exception Information receiver's email if the stmp of the sender's email is available.

    :param sender_email: sender's email
    :param sender_authorization_code:  sender's smtp authorization code
    :param receiver_email: receiver's email or a list of emails
    :param mail_subject: subject of the email
    :param mail_content: content of the email
    :param smtp_host: smtp host address
    :param smtp_port: smtp host port
    :return: smtp server object
    """
    assert isinstance(mail_subject, str), "mail_subject should be given a string"
    assert isinstance(mail_content, str), "mail_content should be given a string"
    assert isinstance(receiver_email, str) or isinstance(receiver_email, list), "receiver_email should be given a string or a list"

    def decorator(fun):
        def wrapper(*args, **kwargs):
            s = config_server(sender_email, sender_authorization_code, smtp_host, smtp_port)
            try:
                result = fun(*args, **kwargs)
                return result
            except Exception as e:
                mail = {
                    'subject': mail_subject,
                    'content_text': mail_content + "\n" + str(e)
                }
                print("sending email...")
                s.send_mail(receiver_email, mail)
                raise e
        return wrapper
    return decorator