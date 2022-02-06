from lib.flask_mailplus import send_template_message
from siapp.app import create_celery_app

celery = create_celery_app()


@celery.task()
def deliver_signup_email(first, last, email):
    """
    Send a signup e-mail.

    :param first: first name of the visitor
    :type first: str
    :param last: last name of the visitor
    :type last: str
    :param email: E-mail address of the visitor
    :type user_id: str
    :return: None
    """
    ctx = {'first': first, 'last': last, 'email': email}

    send_template_message(subject='[siapp] Signup',
                          sender=email,
                          recipients=[celery.conf.get('MAIL_USERNAME')],
                          reply_to=email,
                          template='signup/mail/index', ctx=ctx)

    return None
