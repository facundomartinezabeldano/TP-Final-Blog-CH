from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Blog


def home(request):
    return render(request=request, template_name='home.html', context={})


def about(request):
    return render(request=request, template_name='about.html', context={})


@login_required
def posts(request):
    posts_payload = Blog.objects.all()
    context_payload = {
        'posts': posts_payload
    }
    return render(request=request, template_name='blog_posts.html', context=context_payload)


def create_blog(request):
    # if request.method == 'POST':
    context_payload = {

    }
    return render(request=request, template_name='blog_posts.html', context=context_payload)
