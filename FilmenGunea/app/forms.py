"""
Definition of forms.
"""

from django import forms


class LoginForm(forms.Form):
    erabil = forms.CharField(max_length=100, required=True)
    pasahitza = forms.CharField(widget=forms.PasswordInput, required=True)