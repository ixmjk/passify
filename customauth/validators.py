import string

from django.core.exceptions import ValidationError

from . import constants


class UppercaseValidator:
    def validate(self, password, user=None):
        contains_uppercase = any(char.isupper() for char in password)
        if not contains_uppercase:
            raise ValidationError(
                constants.Messages.PASSWORD_NO_UPPER,
                code="password_no_upper",
            )

    def get_help_text(self):
        return constants.Messages.PASSWORD_NO_UPPER


class LowercaseValidator:
    def validate(self, password, user=None):
        contains_lowercase = any(char.islower() for char in password)
        if not contains_lowercase:
            raise ValidationError(
                constants.Messages.PASSWORD_NO_LOWER,
                code="password_no_lower",
            )

    def get_help_text(self):
        return constants.Messages.PASSWORD_NO_LOWER


class NumberValidator:
    def validate(self, password, user=None):
        contains_digit = any(char.isdigit() for char in password)
        if not contains_digit:
            raise ValidationError(
                constants.Messages.PASSWORD_NO_NUMBER,
                code="password_no_number",
            )

    def get_help_text(self):
        return constants.Messages.PASSWORD_NO_NUMBER


class SymbolValidator:
    def validate(self, password, user=None):
        contains_symbol = any(char in string.punctuation for char in password)
        if not contains_symbol:
            raise ValidationError(
                constants.Messages.PASSWORD_NO_SYMBOL.format(string.punctuation),
                code="password_no_symbol",
            )

    def get_help_text(self):
        return constants.Messages.PASSWORD_NO_SYMBOL.format(string.punctuation)
