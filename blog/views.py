from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post, UserFollowing


def home(request):
    # if username:
    posts = Post.objects.filter(user=request.user)
    return render(request, 'blog/home.html',
                  {'posts': posts})


def post_list(request, username):
    # if username:
    post_owner = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=post_owner)
    return render(request, 'blog/list.html',
                  {'posts': posts})


def all_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/all.html',
                  {'posts': posts})


@login_required
def add_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    user = User.objects.get(id=request.user.id)
    UserFollowing.objects.get_or_create(user=request.user, following=user_to_follow)
    return render(request, 'blog/success.html', {'username': user_to_follow})


@login_required
def delete_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    user = User.objects.get(id=request.user.id)
    UserFollowing.objects.filter(user=request.user, following=user_to_follow).delete()
    return render(request, 'blog/success_to_delete.html', {'username': user_to_follow})


@login_required
def subs_news_list(request):
    # user = User.objects.get(id=request.user.id)
    qs = UserFollowing.objects.filter(user=request.user).values_list('following', flat=True)
    lst_of_ids = list(qs)
    posts = Post.objects.filter(user__in=lst_of_ids).order_by('-date')
    return render(request, 'blog/news.html',
                  {'posts': posts})
