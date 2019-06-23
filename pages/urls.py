from django.urls import path

from . import views 
from .views import  (
 PostListView, 
 PostDetailView,
 PostCreateView,
 PostUpdateView,
 PostDeleteView,
 UserPostListView

 )

urlpatterns = [
    path('', views.home, name ='home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    
    path('contact_us/', views.contact_us, name ='contact_us'),
    path('home/', views.home, name ='home'),
    path('login/', views.login, name ='login'),
    path('team/', views.team, name ='team'),
    path('index/', views.index, name ='index'),

    path('register/', views.register, name ='register'),
    path('blogs/', PostListView.as_view(), name ='blogs'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
   
]