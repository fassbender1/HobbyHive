import threading
from django.core.mail import send_mail
from django.conf import settings


# def async_reminder(email):
#     thread = threading.Thread(target=send_event_reminder, args=(email,))
#     thread.start()


def send_event_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        recipient_list,
        fail_silently=False,
    )


def send_event_reminder_async(user_email, event_title):
    subject = f"Reminder: {event_title}"
    message = f"You have an upcoming event: {event_title}"

    thread = threading.Thread(
        target=send_event_email,
        args=(subject, message, [user_email])
    )
    thread.start()


def notify_participants(event):
    for participation in event.participants.all():
        user = participation.user

        send_event_reminder_async(
            user.email,
            event.title
        )