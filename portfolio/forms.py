from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'class': 'form-input',
                'autocomplete': 'name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'you@email.com',
                'class': 'form-input',
                'autocomplete': 'email',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Subject',
                'class': 'form-input',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Tell me about your project…',
                'class': 'form-input form-textarea',
                'rows': 5,
            }),
        }
