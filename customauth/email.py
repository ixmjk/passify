from django.utils import timezone
from djoser.email import ActivationEmail as BaseActivationEmail
from djoser.email import ConfirmationEmail as BaseConfirmationEmail
from djoser.email import (
    PasswordChangedConfirmationEmail as BasePasswordChangedConfirmationEmail,
)
from djoser.email import PasswordResetEmail as BasePasswordResetEmail
from djoser.email import (
    UsernameChangedConfirmationEmail as BaseUsernameChangedConfirmationEmail,
)
from djoser.email import UsernameResetEmail as BaseUsernameResetEmail
from templated_mail.mail import BaseEmailMessage

from config.context_processors import project_name

from .tasks import send_email_task, send_mass_email_task


class ActivationEmail(BaseActivationEmail):
    def send(self, to, *args, **kwargs):
        self.render()
        send_email_task.delay(
            subject=self.subject,
            message=self.body,
            from_email=self.from_email,
            recipient_list=to,
        )


class ConfirmationEmail(BaseConfirmationEmail):
    def send(self, to, *args, **kwargs):
        self.render()
        send_email_task.delay(
            subject=self.subject,
            message=self.body,
            from_email=self.from_email,
            recipient_list=to,
        )


class PasswordResetEmail(BasePasswordResetEmail):
    def send(self, to, *args, **kwargs):
        self.render()
        send_email_task.delay(
            subject=self.subject,
            message=self.body,
            from_email=self.from_email,
            recipient_list=to,
        )


class UsernameResetEmail(BaseUsernameResetEmail):
    def send(self, to, *args, **kwargs):
        self.render()
        send_email_task.delay(
            subject=self.subject,
            message=self.body,
            from_email=self.from_email,
            recipient_list=to,
        )


class PasswordChangedConfirmationEmail(BasePasswordChangedConfirmationEmail):
    def send(self, to, *args, **kwargs):
        self.render()
        send_email_task.delay(
            subject=self.subject,
            message=self.body,
            from_email=self.from_email,
            recipient_list=to,
        )


class UsernameChangedConfirmationEmail(BaseUsernameChangedConfirmationEmail):
    def send(self, to, *args, **kwargs):
        self.render()
        send_email_task.delay(
            subject=self.subject,
            message=self.body,
            from_email=self.from_email,
            recipient_list=to,
        )


class NewSignInEmail(BaseEmailMessage):
    template_name = "email/new_sign_in.html"

    def send(self, to, *args, **kwargs):
        self.render()
        send_email_task.delay(
            subject=self.subject,
            message=self.body,
            from_email=self.from_email,
            recipient_list=to,
        )


class ReminderEmail(BaseEmailMessage):
    template_name = "email/reminder.html"

    def send(self, to, *args, **kwargs):
        self.context = project_name(None)
        self.render()
        messages = [
            (
                self.subject,
                self.body,
                self.from_email,
                [recipient],
            )
            for recipient in to
        ]
        send_mass_email_task.delay(message_list=messages)
