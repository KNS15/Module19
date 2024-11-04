from django import forms
from .models import Post  # Замените на вашу модель поста

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Укажите поля модели, которые вы хотите использовать

