from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from .views import *
import account.views
import booth.views

app_name='account'

urlpatterns = [
    path('', account.views.login, name='login'),
    path('signup/', account.views.signup, name='signup'),
    path('mypage/<int:pk_id>/', account.views.mypage, name='mypage'),
    path('mypage/<int:pk_id>/boothComment', account.views.myboothComment, name='myboothComment'),
    path('mypage/<int:pk_id>/postComment', account.views.mypostComment, name='mypostComment'),
    path('mypage/boothLike', myLike.as_view(), name='myLike'),
    path('login/', account.views.login, name='login'),
    path('logout/', account.views.logout, name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)