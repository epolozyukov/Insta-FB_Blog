from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [
    
    url(r'^signup/$', views.usersignup, name='register_user'), 
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),
    
    url(r'^view_profile/$', views.view_profile, name ='view_profile'),
    url(r'^view_profile/edit_profile/$', views.edit_profile, name ='edit_profile'),

        
          
]