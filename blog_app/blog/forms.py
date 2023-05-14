from django import forms
from .models import Comment, Post

field_style = 'w-full border border-gray-300 px-3 py-2 rounded-md focus:outline-none focus:border-purple-700'

class CreatePostForm(forms.ModelForm):
    image = forms.ImageField(required=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

    
    def __init__(self, *args, **kwargs):
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = field_style
        self.fields['content'].widget.attrs['class'] = field_style
        self.fields['image'].widget.attrs['class'] = field_style


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': 'Comment'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'class': 'w-full px-4 py-2.5 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500',
            'placeholder': 'Write your comment here...',
            'rows': 4,
        })



