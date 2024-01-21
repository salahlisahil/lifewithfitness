from django.core.mail import send_mail


def subscribe_email(email):
    subject = 'Topic'
    message = 'Text'
    from_email = 'sender@example.com'
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

    pass