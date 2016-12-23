from django import forms


from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    # content = forms.TextField(widget=forms.TextArea, label='Entry')
    class Meta:
        model = Blog
        fields = ["title", "content", "image"]
        # exclude = ['author']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['blog']

