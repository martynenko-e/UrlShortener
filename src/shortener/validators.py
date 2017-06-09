from django.core.validators import URLValidator
from django import forms


def url_validator(value):
    # TODO validate if url start without http://
    url_validator_obj = URLValidator()
    try:
        url_validator_obj(value)
    except:
        raise forms.ValidationError("Invalid url")
    return value