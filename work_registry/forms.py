from django import forms
from .models import Registry

class RegistryAddingForm(forms.ModelForm):
    class Meta:
        model = Registry
        fields =['content']
        labels = {
            'content':'TODO statement:'
        }

    def __init__(self, *args, **kwargs):
        super(RegistryAddingForm, self).__init__(*args, **kwargs)
        # Over-riding attrs.
        self.fields['content'].widget.attrs['rows'] = 11
        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['placeholder'] = 'anything...'
