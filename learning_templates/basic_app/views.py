from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'basic_app/homepage.html')


def other_view(request):
    return render(request, 'basic_app/other.html')


def relative_view(request):
    return render(request, 'basic_app/relative_url_templates.html')
