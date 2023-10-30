from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import User
from first_app.forms import AddUserForm
# Create your views here.


def index(request):
    my_dict = {'insert_me':"Hello I am from views.py of first_app"}
    return render(request, 'first_app/index.html', context=my_dict)

def new_index(request):
    return HttpResponse("<em> Second View </em>")

def main_page(request):
    return HttpResponse('This is Main page of the Project')

def any_page(request):
    return HttpResponse('This is some random page')

def add_user(request):
    empty_form = AddUserForm()

    if request.method == 'POST':
        form_obj = AddUserForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return main_page(request)
    
    return render(request, 'first_app/add_user.html', {'form':empty_form})



def user_page(request):
    user_list = User.objects.all()
    context_dict = {'user_info': user_list}
    return render(request, 'first_app/user_template.html', context=context_dict)
