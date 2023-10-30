from django.shortcuts import render
from django.http import HttpResponse
#from templates import second_app
from second_app.models import Topic, Webpage, AccessRecord

# Create your views here.

def project_page_index(request):
    return HttpResponse("<h1>This is the main page of the Project</h1>")

# Second App homepage
def main_page_index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'second_app/index.html', context=date_dict)

def any_page(request):
    return HttpResponse('This is any other page in the second App')

def temp_page(request):
    temp_data = {'template_data':"This is coming from template tags"}
    return render(request, 'second_app/sample_temp.html', context=temp_data)

def help_page(request):
    template_dict = {'data': 'This is Help Page!!!'}
    return render(request, 'second_app/help_template.html', context=template_dict)

def avi_and_kush_page(request):
    return render(request, 'second_app/static_file_template.html')
