import threading
from django.core.mail import send_mail

def send_event_reminder(email):
    send_mail(
        'Event Reminder',
        'You have an upcoming event!',
        'from@example.com',
        [email],
    )

def async_reminder(email):
    thread = threading.Thread(target=send_event_reminder, args=(email,))
    thread.start()