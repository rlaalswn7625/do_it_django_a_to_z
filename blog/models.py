from django.db import models
from django.contrib.auth.models import User
import os

class Category(models.Model):
    name= models.CharField(max_length=50, unique=True)
    slug= models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=30) # 문자를 담는 필드를 만든다
    hook_text = models.CharField(max_length=100, blank=True)

    content = models.TextField() # textfield는 텍스트의 길이 제한이 없음

    # 게시글이 언제 만들어졌는지 확인해주는 것
    created_at = models.DateTimeField(auto_now_add=True) # 자동으로 수정 시각 저장
    updated_at = models.DateTimeField(auto_now=True)

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
