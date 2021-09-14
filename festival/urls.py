from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path
from . import views


app_name='festival'
urlpatterns = [
    path('', views.collegeList, name='collegeList'),
    path('search/', views.search, name='search'),
    path('searchPost/', views.searchPost, name='searchPost'),
    path('boothsearch/', views.boothsearch, name='boothsearch'),
    path('searchBooth/', views.searchBooth, name='searchBooth'),
    
    path('nursing/', views.nursing, name='nursing'),
    path('nursing/<int:pk_id>', views.detailnursing, name='detailnursing'),
    path('nursing/nursing/<int:pk_id>/comment', views.commentnursing, name='nursingComment'),

    path('convergence/', views.convergence, name='convergence'),
    path('convergence/<int:pk_id>', views.detailconvergence, name='detailconvergence'),
    path('convergence/convergence/<int:pk_id>/comment', views.commentconvergence, name='convergenceComment'),
    
    path('business/', views.business, name='business'),
    path('business/<int:pk_id>', views.detailbusiness, name='detailbusiness'),
    path('business/business/<int:pk_id>/comment', views.commentbusiness, name='businessComment'),
    
    path('pharmacy/', views.pharmacy, name='pharmacy'),
    path('pharmacy/<int:pk_id>', views.detailpharmacy, name='detailpharmacy'),
    path('pharmacy/pharmacy/<int:pk_id>/comment', views.commentpharmacy, name='pharmacyComment'),
    
    path('engineering/', views.engineering, name='engineering'),
    path('engineering/<int:pk_id>', views.detailengineering, name='detailengineering'),
    path('engineering/engineering/<int:pk_id>/comment', views.commentengineering, name='engineeringComment'),
    
    path('music/', views.music, name='music'),
    path('music/<int:pk_id>', views.detailmusic, name='detailmusic'),
    path('music/music/<int:pk_id>/comment', views.commentmusic, name='musicComment'),

    path('social/', views.social, name='social'),
    path('social/<int:pk_id>', views.detailsocial, name='detailsocial'),
    path('social/social/<int:pk_id>/comment', views.commentsocial, name='socialComment'),
    
    path('edu/', views.edu, name='edu'),
    path('edu/<int:pk_id>', views.detailedu, name='detailedu'),
    path('edu/edu/<int:pk_id>/comment', views.commentedu, name='eduComment'),

    path('humanities/', views.humanities, name='humanities'),
    path('humanities/<int:pk_id>', views.detailhumanities, name='detailhumanities'),
    path('humanities/humanities/<int:pk_id>/comment', views.commenthumanities, name='humanitiesComment'),    
    
    path('natural/', views.natural, name='natural'),
    path('natural/<int:pk_id>', views.detailnatural, name='detailnatural'),
    path('natural/natural/<int:pk_id>/comment', views.commentnatural, name='naturalComment'),

    path('scraton/', views.scraton, name='scraton'),
    path('scraton/<int:pk_id>', views.detailscraton, name='detailscraton'),
    path('scraton/scraton/<int:pk_id>/comment', views.commentscraton, name='scratonComment'),

    path('art/', views.art, name='art'),
    path('art/<int:pk_id>', views.detailart, name='detailart'),
    path('art/art/<int:pk_id>/comment', views.commentart, name='artComment'),

    path('hokma/', views.hokma, name='hokma'),
    path('hokma/<int:pk_id>', views.detailhokma, name='detailhokma'),
    path('hokma/hokma/<int:pk_id>/comment', views.commenthokma, name='hokmaComment'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
