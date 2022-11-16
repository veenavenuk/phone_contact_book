from django import forms
from django.contrib.auth.models import User
from .models import *



class PhoneBookContactForm(forms.ModelForm):
    class Meta:
        model = phone_book
        fields = "__all__"


