from django.urls import path

from . import views

urlpatterns =  [
    path('post/<int:blog_post_id>/', views.blog_post, name='blog_post')
]