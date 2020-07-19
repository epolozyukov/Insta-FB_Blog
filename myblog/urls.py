from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [
    
    url(r'^accounts/signup/$', views.usersignup, name='register_user'), 
    url(r'^accounts/activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),
    
    url(r'^view_profile/$', views.view_profile, name ='view_profile'),
    url(r'^edit_profile/$', views.edit_profile, name ='edit_profile'),

    #path("", views.blog_index, name="blog_index"),
    url(r'^blog/$', views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),

        
          
]