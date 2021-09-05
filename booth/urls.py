from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from .views import *
import booth.views

app_name='booth'
urlpatterns = [
    path('', booth.views.boardboothPost, name="boothPost"),
    path('<int:booth_id>', booth.views.detailboothPost, name="detailboothPost"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)