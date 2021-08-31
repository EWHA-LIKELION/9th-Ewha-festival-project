from django.urls import path
from .views import *
import account.views


urlpatterns = [
    path('register/', account.views.register, name='register'),
    path('main/', account.views.main, name='main'),
    path('login/', account.views.login, name='login'),
    path('logout/', account.views.logout, name='logout'),

]