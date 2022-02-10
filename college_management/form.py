from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm
from django.contrib.auth import password_validation
from django.utils.translation import ugettext_lazy as _
from django import forms
class Password_reset(PasswordResetForm):
    email = forms.EmailField(required=True, label="Email",max_length=100,widget=forms.EmailInput(attrs={"autocomplete":"email","class":"form-control","class":"input-material","data-validate-field":"loginUsername"}),help_text=password_validation.password_validators_help_text_html(),)

class Password_confirm(SetPasswordForm):
    password1 = forms.CharField(required=True,label=_("New Password"),widget=forms.PasswordInput(attrs={"autocomplete":"new-password","class":"form-control",}))

    password2 = forms.CharField(required=True, label="Confirm Password",max_length=100,widget=forms.PasswordInput(attrs={"autocomplete":"new-password2","class":"form-control",}))