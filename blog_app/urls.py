from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('blog_posts/', blog_posts, name='blog_posts'),
    path('blog_post/<int:blog_post_id>', blog_post, name='blog_post'),
    path('blog_posts/create/', create_blog_post, name='blog_post_create'),  # ---------------------CRUD [CREATE]
    path('blog_post/delete/<blog_post_id>', delete_blog_post, name='blog_post_delete'),  # --------CRUD [DELETE]
    path('blog_post/edit/<blog_post_id>', edit_blog_post, name='blog_post_edit'),  # --------------CRUD [EDIT]
]

handler404 = "blog_app.views.page_not_found_view"
