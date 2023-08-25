from django import forms

from apps.contacts.models import Contact


class UserForm(forms.ModelForm):
    class Meta:
        model = Contact
        widgets = {
            "password": forms.PasswordInput(),
        }
