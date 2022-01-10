from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('list', views.contact_list, name='list'),
    path('login', views.login_user, name='login'),
    path('logout', views.log_out, name='logout'),
    path('register', views.register, name='register'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('update/<str:pk>', views.update, name='update'),
]