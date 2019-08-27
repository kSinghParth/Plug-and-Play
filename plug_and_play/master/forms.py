from django import forms

class UploadJobForm(forms.Form):
	file = forms.FileField()
	process = forms.FileField()
	aggregate = forms.FileField()
    