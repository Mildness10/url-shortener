from django import forms


class URLSubmissionForm(forms.Form):
    original_url = forms.URLField(label='Enter URL', required=True, widget=forms.URLInput(attrs={'class': 'form-control'}))