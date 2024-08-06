from django.urls import path
from . import views
from  .views import *


app_name="blogpost"
urlpatterns=[
    path("dashboard/",UserDashBoard.as_view(),name="user-dashboard"),   
    path("dashboard/<slug:slug>/", UserDashboardPostDetailView.as_view(), name='user-dashboard-post-detail'),
    path('dashboard/<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
      path('dashboard/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path("writepost",PostCreateView.as_view(),name="post-create"),   
    path("",PostListView.as_view(),name="post-home"),
    path("<slug>/",PostDetailView.as_view(),name="post-detail"),   
   

    
]



