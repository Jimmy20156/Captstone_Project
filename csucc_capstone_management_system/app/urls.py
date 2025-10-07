from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('features', views.features, name='features'),
    path('projects', views.projects, name='projects'),
    path('support', views.support, name='support'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # auth
    path('login/', views.signin, name='login'),
    path('register', views.register, name='register'),
    path('logout/', views.signout, name='logout'),
]