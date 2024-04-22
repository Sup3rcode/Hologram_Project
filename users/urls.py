from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'users'
urlpatterns = [
    path('signup/',views.signup,name='register'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('settings/change_password/',auth_views.PasswordChangeView.as_view(template_name='users/change_password.html'),name='password_change'),
    path('settings/change_password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='users/change_password_done.html'),name='password_change_done'),
    path('Update_Profile/<int:usr_id>/',views.new_topic,name='Update_Profile') ,
    
]
