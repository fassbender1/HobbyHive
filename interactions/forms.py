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

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content.strip()) < 2:
            raise forms.ValidationError("Comment is too short.")
        return content