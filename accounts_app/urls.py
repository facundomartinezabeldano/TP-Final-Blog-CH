from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', view=login, name='login'),
    path('log-out/', view=LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('sign-up/', view=sign_up, name='sign-up'),
    path('edit_user/', view=edit_user, name='edit-user'),
]
