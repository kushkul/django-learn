from django.shortcuts import render
from basicApp import forms
# Create your views here.

def homepage(request):
    return render(request, 'basicApp/homepage.html')

def formname_view(request):
    form_obj = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

    return render(request, 'basicApp/form.html', {'form':form_obj})
