from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        # specify model to be used
        model = Contact

        # specify fields to be used
        fields = [
            "contact_name",
            "contact_email",
            "contact_notes",
        ]

        labels = {
            'contact_name': 'Name',
            'contact_email': 'Email',
            'contact_notes': 'Notes',
        }