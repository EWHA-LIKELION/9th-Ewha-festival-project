from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.boardboothPost, name="boothPost"),
    path('<int:pk_id>', views.detailboothPost, name="detailboothPost"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)