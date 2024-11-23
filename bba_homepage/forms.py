from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.CharField(label='', validators=[EmailValidator()], widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    phone = forms.CharField(label='', max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    subject = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Message'}))
    