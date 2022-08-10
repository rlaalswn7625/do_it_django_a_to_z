from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField() # textfield는 텍스트의 길이 제한이 없음

    # 게시글이 언제 만들어졌는지 확인해주는 것
    created_at = models.DateTimeField(auto_now_add=True) # 자동으로 수정 시각 저장
    updated_at = models.DateTimeField(auto_now=True)
    # 언젠가 작성자를 추후 만들거다

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'