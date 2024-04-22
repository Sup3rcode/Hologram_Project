from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import widgets
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from django import forms
from .models import *


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput())

    class Meta:
        model=User
        fields = {'username','email','password1','password2'}



class ProfileForm(forms.ModelForm):
   
    class Meta:
        model=Profile
        fields = {'bio','avatar'}
       
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-input form-control-has-validation',
                
            })        

