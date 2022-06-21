from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('create_blog/', create_blog_post, name='create.blog')
]
