import logging

from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import BadHeaderError, send_mail, send_mass_mail
from djoser.conf import settings

User = get_user_model()
logger = logging.getLogger(__name__)


@shared_task
def send_email_task(subject, message, from_email, recipient_list):
    try:
        logger.info("[send_email_task] Sending email...")
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
        )
        logger.info("[send_email_task] Email sent successfully!")
    except BadHeaderError as e:
        logger.error(f"[send_email_task] BadHeaderError: {e}")


@shared_task
def send_mass_email_task(message_list):
    try:
        logger.info("[send_mass_email_task] Sending emails...")
        send_mass_mail(
            message_list,
            fail_silently=False,
        )
        logger.info("[send_mass_email_task] Emails sent successfully!")
    except BadHeaderError as e:
        logger.error(f"[send_mass_email_task] BadHeaderError: {e}")


@shared_task
def notify_users_task():
    try:
        if settings.SEND_REMINDER_EMAIL:
            users = User.objects.filter(is_active=True)
            to = [user.email for user in users]
            if to:
                settings.EMAIL.reminder().send(to)
        else:
            logger.warning(
                "[notify_users_task] SEND_REMINDER_EMAIL is off.",
            )
    except Exception as e:
        logger.error(f"[notify_users_task] Exception: {e}")
