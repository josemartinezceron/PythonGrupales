from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.register, name='signup'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
