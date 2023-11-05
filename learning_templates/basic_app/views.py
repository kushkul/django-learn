from django.shortcuts import render

# Create your views here.


def homepage(request):
    context_dict = {'text':'Kush Kulshrestha',
                    'number':100}
    return render(request, 'basic_app/homepage.html', context_dict)


def other_view(request):
    return render(request, 'basic_app/other.html')


def relative_view(request):
    return render(request, 'basic_app/relative_url_templates.html')
