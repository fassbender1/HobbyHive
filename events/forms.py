from django import forms
from .models import Event
from .models import EventParticipation

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('organizer',)

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Event title'}),
            'location': forms.TextInput(attrs={'placeholder': 'Event location'}),
            'date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            })
        }

        error_messages = {
            'title': {'required': 'Event title is required!'}
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        from django.utils.timezone import now
        if date <= now():
            raise forms.ValidationError("Event must be scheduled in the future.")
        return date

class RSVPForm(forms.ModelForm):
    class Meta:
        model = EventParticipation
        fields = ('status',)

        labels = {
            'status': 'Your Response',
        }