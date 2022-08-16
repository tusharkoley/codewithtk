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

urlpatterns= [

path('', PostListView.as_view(), name ='blogs'),
path('<int:pk>/', PostDetailView.as_view(),name="post-detail"),
path('comment/reply/', views.reply_page, name="reply"), 
path('new/', PostCreateView.as_view(), name='post-create'),
path('<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
# path('<slug:post>/',views.post_detail,name="post_detail"),
# path('comment/reply/', views.reply_page, name="reply"), #


]
