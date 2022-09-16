from django import forms
from project4.settings import POSTLENGTH

class NewPost(forms.Form):
    body = forms.CharField(label='', max_length=POSTLENGTH, widget=forms.Textarea(attrs={'class': 'NewPostBody'}))