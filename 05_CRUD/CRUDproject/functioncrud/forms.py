from django import forms
from .models import Blog

class NewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        # 모든 model을 입력받고 싶으면 fields = '__all__'
        fields = ['title', 'body']