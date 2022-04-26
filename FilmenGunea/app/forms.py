"""
Definition of forms.
"""

from django import forms


class LoginForm(forms.Form):
    usr = forms.CharField(max_length=100, required=True, label='Erabiltzailea')
    pswd = forms.CharField(widget=forms.PasswordInput, required=True, label='Pasahitza')

class RegisterForm(forms.Form):
    usr = forms.CharField(max_length=100, required=True, label='Erabiltzilea')
    pswd = forms.CharField(widget=forms.PasswordInput, min_length=8, required=True, label='Pasahitza')
    pswd2 = forms.CharField(widget=forms.PasswordInput, min_length=8, required=True, label='Errep. pasahitza')