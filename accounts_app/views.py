from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.shortcuts import render

from .forms import UserSignInForm, UserEditForm


def login(request):
    home_template = 'blog_app/index.html'
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_payload = authenticate(username=user, password=password)

            if user_payload is not None:
                auth_login(request, user_payload)
                return render(request=request, template_name=home_template, context={'message': f'Welcome {user}'})

            else:
                return render(request=request, template_name=home_template, context={'message': "Login error your credentials weren't right"})

        else:
            return render(request=request, template_name=home_template, context={'message': 'Form Error'})

    form = AuthenticationForm()

    return render(request=request, template_name='login.html', context={'form': form})


def sign_up(request):
    home_template = 'blog_app/index.html'
    if request.method == 'POST':
        form = UserSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request=request, template_name=home_template, context={'message_creation': f'User: {username} has been created successfuly'})
        else:
            return render(request=request, template_name=home_template, context={'message_creation': f'Error username was created wrong'})
    else:
        form = UserSignInForm()
    return render(request=request, template_name='sign_up.html', context={'form': form})


@login_required
def edit_user(request):
    u = request.user
    if request.method == 'POST':
        user_edit_form = UserEditForm(request.POST, instance=u)
        if user_edit_form.is_valid():
            user_payload = user_edit_form.cleaned_data()

            u.email = user_payload['email']
            u.password1 = user_payload['password1']
            u.password2 = user_payload['password2']
            u.save()
            return render(request=request, template_name='index.html', context={'message': 'User Edited Successfuly'})
    else:
        user_edit_form = UserEditForm(initial={
            'email': u.email
        })
    return render(request=request, template_name='edit_user.html', context={
        'user_edit_form': user_edit_form,
        'u': u
    })
