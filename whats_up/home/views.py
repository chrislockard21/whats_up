from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm

# Create your views here.

class Index(View):

    template_name = 'templates/home/index.html'
    
    def get(self, request):
        
        context = {
            
        }
        
        return render(request, self.template_name, context)

class Registration(View):

    form_class = UserForm
    template_name = 'templates/home/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            print(request.POST)
            user = form.save(commit=False)

            # Clean the data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('/sucess/')

        return render(request, self.template_name, {'form':form})

class Sucess(View):

    template_name = 'templates/home/sucess.html'

    def get(self, request):
        return render(request, self.template_name)

class Login(View):
    '''
    Renders the login page
    '''
    template_name = 'home/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_failed = True
            return render(request, self.template_name, {'login_failed':login_failed})

class Logout(View):
    '''
    Logs the user out and returns them to the home page
    '''
    template_name = 'templates/home/index.html'

    def get(self, request):
        logout(request)
        return redirect('/')
    
