#from django.conf.urls import url
from basic_app import views
from django.urls import path, re_path

# For using TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    re_path(r"^relative/$", views.relative_view, name="relative"),
    re_path(r"^other/$", views.other_view, name="other"),
]


