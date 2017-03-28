from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls
