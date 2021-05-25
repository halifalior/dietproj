from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age','gender','weight','hight','isveg']


