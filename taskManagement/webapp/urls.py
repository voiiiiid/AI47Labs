from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.logout, name="logout"),
    path('create-task', views.create, name="create-task"),
    path('update-task/<int:pk>', views.update, name="update-task"),
    path('view-task/<int:pk>', views.view, name="view-task"),
    path('delete-task/<int:pk>', views.delete, name="delete-task"),
    path('social-auth', include('social_django.urls'), name='social'),
]
