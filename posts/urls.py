from django.urls import path
from . import views
from  .views import *


app_name="blogpost"
urlpatterns=[
    path("dashboard/",user_dashboard,name="user-dashboard"),   
    path("writepost",PostCreateView.as_view(),name="post-create"),   
    path("",PostListView.as_view(),name="post-home"),
    path("<slug>/",PostDetailView.as_view(),name="post-detail"),   
    path('<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),

    
]



