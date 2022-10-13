from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    helper = FormHelper()
    helper.add_input(Submit("submit", "Submit", css_class="btn-primary"))
    helper.add_input(
        Button(
            "cancel",
            "Cancel",
            css_class="btn",
            onclick=f"javascript:location.href = '/physicians/';",
        )
    )
    helper.form_method = "POST"

    class Meta:
        model=User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]