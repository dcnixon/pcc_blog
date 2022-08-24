from django import forms

from .models import BlogPost


class EntryForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Title:', 'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}