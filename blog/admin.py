from django.contrib import admin
from .models import Post, UserFollowing


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'date', 'id']
    list_filter = ['title', 'date']


@admin.register(UserFollowing)
class UserFollowingAdmin(admin.ModelAdmin):
    list_display = ['user', 'following']
