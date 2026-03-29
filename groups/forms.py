from django import forms
from .models import Group

class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = ('owner', 'members', 'created_at')

        labels = {
            'name': 'Group Name',
            'description': 'About the Group',
        }

        help_texts = {
            'name': 'Choose a unique and catchy name.',
            'description': 'Describe what your group is about.',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. Sofia Hiking Club'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Tell people what this group is about...'
            }),
        }

        error_messages = {
            'name': {
                'required': 'Group name is mandatory!',
            }
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Group name must be at least 3 characters.")
        return name

class GroupUpdateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].disabled = True

class GroupDeleteForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance