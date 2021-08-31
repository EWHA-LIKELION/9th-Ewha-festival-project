from django.urls import path
from . import views

urlpatterns = [
    path('', views.collegeList, name='collegeList'),
    path('search', views.search, name='search'),
]
