from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", TaskView.as_view(), name= "tasks_list_url")
]