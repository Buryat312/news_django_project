from django import forms
from comments.models import Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body' ]

        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.Textarea(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),

    }


