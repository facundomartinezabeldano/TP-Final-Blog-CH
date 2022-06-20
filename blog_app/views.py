from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Blog


def home(request):
    return render(request=request, template_name='home.html', context={})


def about(request):
    return render(request=request, template_name='about.html', context={})


@login_required
def blog_posts(request):
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


def blog_post(request, blog_post_id):
    blog_post_payload = Blog.objects.get(id=blog_post_id)
    context_payload = {
        'blog_post': blog_post_payload
    }
    return render(request=request, template_name='blog_post.html', context=context_payload)



def page_not_found(request, exeption):
    return render(request=request, template_name='404.html', context={})
