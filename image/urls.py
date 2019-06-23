from django.urls import path

from . import views

app_name = 'image'
urlpatterns = [
    path('', views.ImageCreateView.as_view(), name='edge'),

    path('list', views.results, name='list'),

    path('list/<int:pk>/delete/', views.ImgtDeleteView.as_view(), name='del'),
 

]