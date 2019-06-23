from django.urls import path

from . import views

app_name = 'scrap'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.IndexCreateView.as_view(), name='new'),
    path('<int:index_id>/', views.results, name='detail')
    #path('<int:pk>/', views.DetailView.as_view(), name='detail')
    ]