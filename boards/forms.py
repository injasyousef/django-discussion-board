from django import forms
from .models import Topic,Post

class NewTobicForm(forms.ModelForm):


    message=forms.CharField(widget=forms.Textarea(
        attrs={'rows':5,'placeholder':'What in your mind?'}
    ),
    max_length=4000,
    help_text='the max length of the text is 4000')


    class Meta:
        model = Topic
        fields=['subject','message']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['message',]

