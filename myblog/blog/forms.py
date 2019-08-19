from django import forms
from .models import Comment

class FormComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            'text': "Comment"
        }
        widgets = {
            'text': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }

