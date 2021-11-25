from django.forms import ModelForm,HiddenInput
from .models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = [ 'email', 'subject', 'message']