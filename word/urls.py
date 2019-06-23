from django.urls import path

from . import views

app_name = 'word'
urlpatterns = [
    path('', views.resume, name='word')


]