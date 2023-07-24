from .models import Comment
from django import forms

class PostForm(forms.Form):
    image = forms.FileField()
    text = forms.CharField(label="Name")
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Describe what does the image represents'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'country', 'body')