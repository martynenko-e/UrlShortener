from django import forms
from .validators import url_validator


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='submit url', validators=[url_validator])

    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     url = cleaned_data['url']
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid url")
    #     print url

