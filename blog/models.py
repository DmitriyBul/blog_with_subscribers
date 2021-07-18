from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class UserFollowing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following_posts', verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followed_by', on_delete=models.CASCADE)

class AlreadyRead(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_read', verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='read_id', on_delete=models.CASCADE)