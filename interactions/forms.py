from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your comment...'
            })
        }

    def clean(self):
        cleaned_data = super().clean()

        group = cleaned_data.get('group')
        event = cleaned_data.get('event')

        if not group and not event:

            return cleaned_data

        return cleaned_data