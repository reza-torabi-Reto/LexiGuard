from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Word(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='users')
    word_eng = models.CharField(max_length=200, verbose_name='words')
    word_fa = models.CharField(max_length=200, verbose_name='words')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.word_eng