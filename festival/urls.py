from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.collegeList, name='collegeList'),
    path('search/', views.search, name='search'),
    
    path('nursing/', views.nursing, name='nursing'),
    path('nursing/<int:pk_id>', views.detailnursing, name='detailnursing'),
    
    path('convergence/', views.convergence, name='convergence'),
    path('convergence/<int:pk_id>', views.detailconvergence, name='detailconvergence'),
    
    path('business/', views.business, name='business'),
    path('business/<int:pk_id>', views.detailbusiness, name='detailbusiness'),
    
    path('pharmacy/', views.pharmacy, name='pharmacy'),
    path('pharmacy/<int:pk_id>', views.detailpharmacy, name='detailpharmacy'),
    
    path('engineering/', views.engineering, name='engineering'),
    path('engineering/<int:pk_id>', views.detailengineering, name='detailengineering'),
    
    path('music/', views.music, name='music'),
    path('music/<int:pk_id>', views.detailmusic, name='detailmusic'),
    
    path('social/', views.social, name='social'),
    path('social/<int:pk_id>', views.detailsocial, name='detailsocial'),
    
    path('edu/', views.edu, name='edu'),
    path('edu/<int:pk_id>', views.detailedu, name='detailedu'),

    path('humanities/', views.humanities, name='humanities'),
    path('humanities/<int:pk_id>', views.detailhumanities, name='detailhumanities'),
    
    path('natural/', views.natural, name='natural'),
    path('natural/<int:pk_id>', views.detailnatural, name='detailnatural'),

    path('scraton/', views.scraton, name='scraton'),
    path('scraton/<int:pk_id>', views.detailscraton, name='detailscraton'),

    path('art/', views.art, name='art'),
    path('art/<int:pk_id>', views.detailart, name='detailart'),

    path('hokma/', views.hokma, name='hokma'),
    path('hokma/<int:pk_id>', views.detailhokma, name='detailhokma'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
