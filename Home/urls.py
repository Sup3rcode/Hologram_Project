from django.urls import path
from . import views


app_name = 'Home'
urlpatterns = [
    path('', views.index, name="index"),
    path('All_Article/', views.View_All_Article, name="All_Article"),
    path("Home/Articles/detail/<int:Articles_id>/", views.Articles_idDetailView, name="Home_Articles_detail"),
    path('All_Gallery/', views.View_All_Gallery, name="All_Gallery"),
    path('All_video/', views.View_All_video, name="All_video"),
]