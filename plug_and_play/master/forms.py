from django import forms

class UploadJobForm(forms.Form):
    process = forms.FileField()
    aggregate = forms.FileField()
    