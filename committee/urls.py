from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from . import views

app_name='committee'
urlpatterns = [
    path('', views.committeeList, name="committeeList"),
    path('<int:pk_id>', views.detailcommitteePost, name="detailcommitteePost"),
    path('committee/<int:pk_id>/comment',views.commentcommittee,name='committeeComment')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    