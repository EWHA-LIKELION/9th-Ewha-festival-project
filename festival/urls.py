from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.collegeList, name='collegeList'),
    path('search', views.search, name='search'),
    path('college/<str:college_id>', views.boardcollegePost, name='boardcollegePost'),
    path('college/<str:college_id>/<int:pk_id>', views.detailcollegePost, name='detailcollegePost'),
    path('booth/', views.boardboothPost, name='boardboothPost'),
    path('booth/<int:booth_id>', views.detailboothPost, name='detailboothPost'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
