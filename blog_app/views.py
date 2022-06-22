from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import CreateBlogForm, EditBlogForm


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


def blog_post(request, blog_post_id):
    blog_post_payload = Blog.objects.get(id=blog_post_id)
    context_payload = {
        'blog_post': blog_post_payload
    }
    return render(request=request, template_name='blog_post.html', context=context_payload)


def create_blog_post(request):
    if request.method == 'POST':
        create_blog_post_form = CreateBlogForm(request.POST)
        if create_blog_post_form.is_valid():
            blog_post_clean_payload = create_blog_post_form.cleaned_data
            title = blog_post_clean_payload['title']
            sub_title = blog_post_clean_payload['sub_title']
            body = blog_post_clean_payload['body']
            author = blog_post_clean_payload['author']
            new_blog_post = Blog(
                title=title,
                sub_title=sub_title,
                body=body,
                author=author
            )
            new_blog_post.save()

            context = {
                'message': 'Post created successfuly'
            }

            return render(request=request, template_name='blog_posts.html', context=context)
    else:
        create_blog_post_form = CreateBlogForm()
        context_payload = {
            'create_blog_post_form': create_blog_post_form
        }
    return render(request=request, template_name='create_blog_post.html', context=context_payload)


def delete_blog_post(request, blog_post_id):
    try:
        blog_post_payload = Blog.objects.get(id=blog_post_id)
        blog_post_payload.delete()
    except:
        context = {
            'message': 'Error (probably wrong blog post id)'
        }
        return render(request=request, template_name='home.html', context=context)
    return render(request=request, template_name='delete_blog_post.html', context={})


def edit_blog_post(request, blog_post_id):
    blog_post = Blog.objects.get(id=blog_post_id)
    if request.method == 'POST':
        edit_blog_post_form = EditBlogForm(request.POST)
        if edit_blog_post_form.is_valid():
            payload = edit_blog_post_form.cleaned_data
            blog_post.title = payload['title'],
            blog_post.sub_title = payload['sub_title']
            blog_post.body = payload['body']
            blog_post.author = payload['author']
            blog_post.save()

            blog_posts = Blog.objects.all()
            context = {'posts': blog_posts}
            return render(request, 'blog_posts.html', context=context)
    else:
        edit_blog_post_form = EditBlogForm(initial={
            'title': blog_post.title, 'sub_title': blog_post.sub_title, 'body': blog_post.body, 'author': blog_post.author})
        context = {'edit_blog_post_form': edit_blog_post_form,
                   'blog_post_id': blog_post.id}
        return render(request, 'edit_blog_post.html', context=context)


def page_not_found(request, exeption):
    return render(request=request, template_name='404.html', context={})
