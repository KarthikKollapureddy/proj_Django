from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import User,MoM,feedback
from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

class MoMForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = MoM
        fields = ['date','action_items','focus_points']

class feedbackForm(ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'