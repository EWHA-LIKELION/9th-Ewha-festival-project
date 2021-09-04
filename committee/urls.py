from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from . import views

app_name='committee'
urlpatterns = [
    path('', views.committeeList, name="committeList"),
    path('<int:pk_id>', views.detailcommitteePost, name="detailcommitteePost")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    