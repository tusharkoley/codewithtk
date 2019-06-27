from django.urls import path

from . import views



urlpatterns =[

path('',views.gallery, name='gallery'),
path('<slug>/', views.AlbumDetail.as_view(), name='album'), #app.views.AlbumView.as_view()



]
