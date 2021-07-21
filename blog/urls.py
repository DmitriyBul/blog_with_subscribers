from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('profile/<str:username>/', views.post_list, name='post_list'),
    # path('<int:id>/', views.post_list, name='post_list'),
    path('latest/', views.all_list, name='all_list'),
    path('success/<str:username>/', views.add_user, name='add_user'),
    path('news/', views.subs_news_list, name='news_list'),
    path('successtodelete/<str:username>/', views.delete_user, name='delete_user'),
    path('home/', views.home, name='home'),
    path('add/', views.post_create, name='post_create'),
    path('alreadyread/<int:post_id>', views.already_read, name='already_read'),
]
