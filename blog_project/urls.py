"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog_app.views import *
from accounts_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('blog_posts/', blog_posts, name='blog_posts'),
    path('blog_post/<blog_post_id>', blog_post, name='blog_post'),
    path('blog_post/delete/<blog_post_id>',
         delete_blog_post, name='blog_post_delete'),
    path('blog/', include('blog_app.urls')),
    path('accounts/', include('accounts_app.urls')),
]

handler404 = 'blog_app.views.page_not_found'
