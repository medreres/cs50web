from email.policy import default
from sre_parse import CATEGORIES
from unicodedata import category
from attr import attr, attrs
from django import forms
from commerce.settings import CATEGORIESCHOICES


class LoginForm(forms.Form):
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


class CreateListing(forms.Form):
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(attrs={'autofocus': 'autofocus', 'required': 'required'}))
    description = forms.CharField(
        label='Description', widget=forms.Textarea(), required=False)
    price = forms.DecimalField(label='Price', required=True)

    img = forms.URLField(label='URL',  widget=forms.TextInput(
        attrs={'placeholder': 'optional'}), required=False,)

    category = forms.ChoiceField(
        widget=forms.Select, choices=CATEGORIESCHOICES, required=False)


class MakeBid(forms.Form):
    price = forms.DecimalField(label="Price", required=True)


class MakeComment(forms.Form):
    text = forms.CharField(label='',
                           widget=forms.TextInput(attrs={'style': "width: 100%; height: 100%;", "align": 'center', 'autocomplete': 'off', }))
