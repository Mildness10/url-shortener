from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

#form to handle url submission
class URLSubmissionForm(forms.Form):
    original_url = forms.URLField(label='Enter URL', required=True, widget=forms.URLInput(attrs={'class': 'form-control'}))

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']