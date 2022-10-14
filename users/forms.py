from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Button

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
        fields = ['first_name','last_name','email','password1','password2',]