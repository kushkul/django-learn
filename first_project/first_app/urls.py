from django.urls import path, re_path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'kush.', views.any_page, name='any_page'),
]