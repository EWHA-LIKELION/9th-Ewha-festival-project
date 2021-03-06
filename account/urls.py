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
    path('mypage/', account.views.mypage, name='mypage'),
    path('mypage/boothComment', account.views.myboothComment, name='myboothComment'),
    path('mypage/postComment', account.views.mypostComment, name='mypostComment'),
    path('mypage/boothLike', account.views.myLike, name='myLike'),
    path('login/', account.views.login, name='login'),
    path('logout/', account.views.logout, name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)