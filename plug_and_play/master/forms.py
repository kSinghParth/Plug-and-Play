from django import forms

class NameForm(forms.Form):
    process = forms.FileField()
    