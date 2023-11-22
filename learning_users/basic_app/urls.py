#from django.conf.urls import url
from django.urls import path
from basic_app import views

# Template Urls!
app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name='register')
]