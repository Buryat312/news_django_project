from django.shortcuts import redirect, render, reverse
from django.views import View
from accounts.forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

class LoginView(View):

    def get(self, request):

        if request.user.is_authenticated:
            return redirect(reverse('post_list_url'))

        login_form = LoginForm()
        
        return render(request, 'accounts/login.html', context={'login_form': login_form})

    def post(self, request):

        bound_form = LoginForm(request.POST)
        if bound_form.is_valid():
            username = bound_form.cleaned_data.get('username')
            password = bound_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect(reverse('post_list_url'))
        return render(request, 'accounts/login.html', context={'login_form': bound_form})

class RegistrationView(View):

    def get(self, request):

        if request.user.is_authenticated:
            return redirect(reverse('post_list_url'))

        register_form = RegistrationForm()
        
        return render(request, 'accounts/registration.html', context={'register_form': register_form})

    def post(self, request):
        User = get_user_model()
        print(request.user.username)
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            username = registration_form.cleaned_data.get('username')
            password = registration_form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect(reverse('post_list_url'))
        return render(request, 'accounts/registration.html', context={'registration_form':registration_form})