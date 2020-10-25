from django.test import TestCase
from django.core.mail import send_mail


class TestContactPage(TestCase):
    def test_send_mail(self):
        send_mail('Testing', 'Here is the message.', 'from@example.com', ['mail.pythonsuli@gmail.com'], fail_silently=False)