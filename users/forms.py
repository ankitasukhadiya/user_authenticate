from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Button
from django.contrib.auth.forms import \
    AuthenticationForm as BaseAuthenticationForm
from .models import User

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

# class PasswordChangingForm(PasswordChangeForm):
#     old_password = forms.CharField(widget =forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
#     new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
#     new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}) )

#     class Meta:
#         model = User
#         fields = ('old_password','new_password1','new_password2')