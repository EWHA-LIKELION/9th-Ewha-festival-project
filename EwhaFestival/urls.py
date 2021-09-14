"""EwhaFestival URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler500
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
import festival.views
import account.views
import booth.views
import committee.views
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('F2ACB3A84DD5F6578311EE348DE737C0895CF4156D12A0E49F89F284AA53F9AF/', admin.site.urls),
    path('', festival.views.main, name='main'),
    path('account/', include('account.urls')),
    path('festival/', include('festival.urls')),
    path('booth/', include('booth.urls')),
    path('committee/', include('committee.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "festival.views.page_not_found_view"
handler500 = "festival.views.sever_error"