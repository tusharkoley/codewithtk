from django import forms
from blogs.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('title','content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
