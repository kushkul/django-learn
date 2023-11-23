from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def homepage(request):
    return render(request, 'basic_app/homepage.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) #Hashing the password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            registered = True
        
        else:
            print(user_form.errors, profile_form.errors)
    
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    #print('Current value of registered: {}'.format(registered))
    return render(request, 'basic_app/registration.html', 
                      {'user_form': user_form, 
                       'profile_form': profile_form,
                       'registered': registered})


def user_login(request):

    if request.method == 'POST':
        # Get use name and password of the user
        username = request.POST.get('username')
        password= request.POST.get('password')

        # Automatically authenticate the code
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                return HttpResponse('Account not active')
        else:
            print('Username doesnot exits: {}'.format(username))
            return HttpResponse("Invalid login details specified")
    
    else:
        return render(request, 'basic_app/login.html', {})


# Decorator to ensure this view is only accessible if user has logged in
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
    
@login_required
def login_status(request):
    return HttpResponse('You are logged in now')

