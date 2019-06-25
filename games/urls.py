from django.urls import path

from . import views

app_name='games'

urlpatterns =[

path('',views.index, name='index'),
path('connect4/',views.connect4, name='connect4'),
path('tt_toe/',views.tt_toe, name='tt_toe'),


]
