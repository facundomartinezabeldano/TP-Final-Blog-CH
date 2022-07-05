from django.contrib import admin
from django.urls import path, include
from blog_app.views import *
from accounts_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('blogs/', include('blog_app.urls')),
    path('accounts/', include('accounts_app.urls')),
]
handler404 = "blog_app.views.page_not_found_view"
