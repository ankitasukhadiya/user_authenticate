from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Button
from django.contrib.auth.forms import \
    AuthenticationForm as BaseAuthenticationForm
from django.forms import ModelForm
from .models import User,Image
# from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    helper = FormHelper()
    helper.add_input(Submit("submit", "Submit",css_class = 'btn'))
    helper.add_input(
        Button(
            "cancel",
            "Cancel",
            css_class="btn",
            onclick=f"javascript:location.href = '/users/';",
        )
    )
    helper.form_method = "POST"

    class Meta:
        model=User
        fields = ['first_name','last_name','email','password1','password2']

class AuthenticationForm(BaseAuthenticationForm):
    helper = FormHelper()
    helper.add_input(
        Submit("submit", "Login", css_class="btn-pink btn-block text-uppercase")
    )
    helper.form_method = "POST" 

class ChangePasswordForm(PasswordChangeForm):
    helper = FormHelper()
    helper.add_input(Submit("submit", "Change Password",css_class = 'btn'))
    helper.add_input(
        Button(
            "cancel",
            "Cancel",
            css_class="btn",
            onclick=f"javascript:location.href = '/users/';",
        )
    )
    helper.form_method = "POST"

class ImageForm(forms.ModelForm):
    helper = FormHelper()
    helper.add_input(Submit("submit", "Submit",css_class = 'btn'))
    helper.add_input(
        Button(
            "cancel",
            "Cancel",
            css_class="btn",
            onclick=f"javascript:location.href = '/users/';",
        )
    )
    helper.form_method = "POST"

    class Meta:
        model=Image
        fields = ['image']
