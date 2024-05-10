from django.utils.translation import gettext_lazy as _


class Messages:
    PASSWORD_NO_UPPER = _("Password must contain at least 1 uppercase letter: A-Z.")
    PASSWORD_NO_LOWER = _("Password must contain at least 1 lowercase letter: a-z.")
    PASSWORD_NO_NUMBER = _("Password must contain at least 1 digit: 0-9.")
    PASSWORD_NO_SYMBOL = _("password must contain at least 1 symbol: {0}")
