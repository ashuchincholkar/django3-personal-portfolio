from django import forms
from .models import ContactME


class ContactMeForm(forms.ModelForm):

    class Meta:
        model = ContactME
        fields = ['name', 'email', 'subject', 'message']
        