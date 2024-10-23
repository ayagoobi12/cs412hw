from django import forms
from .models import StatusMessage

class CreateStatusMessageForm(forms.ModelForm):
    class Meta:
        model = StatusMessage  # Specify the model to use
        fields = ['message']  # List the fields you want in the form

    # Add any additional methods or validation here if necessary