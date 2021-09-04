from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('committee/', views.committeeList, name="committeList"),
    path('committee/<int:pk_id>', views.detailcommitteePost, name="detailcommitteePost")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    