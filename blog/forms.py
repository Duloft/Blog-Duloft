from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *


class BlogPostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Title'
            }
        ))
    content = forms.CharField(widget=FroalaEditor)
    
    class Meta:
        model = PostModel
        fields = ['title', 'content', 'image']
        
    def save (self, commit=True):
        blog_post = self.instance
        blog_post.title = self.cleaned_data['title']
        blog_post.content = self.cleaned_data['content']
        
        if self.cleaned_data['image']:
            blog_post.image = self.cleaned_data['image']
            
        if commit:
            blog_post.save
        return blog_post