from django import forms
from .validators import url_validator


class SubmitUrlForm(forms.Form):
    url = forms.CharField(
        label='',
        validators=[url_validator],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Long Url",
                "class": "form-control"
            }
        )
        )

