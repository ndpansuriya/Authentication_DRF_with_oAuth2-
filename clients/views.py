from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer

from rest_framework import viewsets, permissions

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


class UserViewSet(viewsets.ModelViewSet):
    """
        ViewSet for Clients
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer
