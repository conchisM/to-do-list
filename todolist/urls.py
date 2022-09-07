from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    #Todos
    path('current/', views.currenttodos, name='currenttodos'),
    path('create/', views.createtodo, name='createtodo'),
    path('', views.home, name='home'),
]
