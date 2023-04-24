from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logoutPage'),
    path('logged_in/',views.logged_in,name='logged_in'),
    path('mom/',views.MoMPage,name='MoMPage'),
    path('feedback/',views.feedbackPage,name='feedbackPage'),
    path('mentee/register/', views.mentee_register, name='mentee_register'),
    path('mentor/register/', views.mentor_register, name='mentor_register'),
]
