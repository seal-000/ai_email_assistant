# forms.py
from django import forms

class RephraseForm(forms.Form):
    text_to_rephrase = forms.CharField(widget=forms.Textarea, label='Enter text to convert into a professional email')
