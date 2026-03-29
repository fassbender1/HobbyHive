from django.core.exceptions import ValidationError
import re


def validate_min_length(value, min_length=3):
    if len(value.strip()) < min_length:
        raise ValidationError(f"Must be at least {min_length} characters long.")


def validate_no_special_characters(value):
    if not re.match(r'^[a-zA-Z0-9\s]+$', value):
        raise ValidationError("Only letters, numbers, and spaces are allowed.")


def validate_starts_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Must start with a letter.")


def validate_future_date(value):
    from django.utils.timezone import now
    if value <= now():
        raise ValidationError("Event date must be in the future.")


def validate_not_empty(value):
    if not value.strip():
        raise ValidationError("This field cannot be empty.")