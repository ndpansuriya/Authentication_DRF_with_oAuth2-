from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [

    url(r'^', include('clients.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

]

admin.site.site_header = 'Authentication Module oAuth2'
