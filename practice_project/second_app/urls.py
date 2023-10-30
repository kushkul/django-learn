from django.urls import path, re_path    
from second_app import views


urlpatterns = [
    path('', views.main_page_index, name='main_page'),
    #re_path(r'k.', views.any_page, name='any_page'),
    path('template', views.temp_page, name='template_view'),
    path('help', views.help_page, name='help_page'),
    path('avi_kush', views.avi_and_kush_page, name='avi_and_kush')
]