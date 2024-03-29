from django.contrib.auth.models import User
from django.db.models.manager import BaseManager
from rest_framework import generics
from rest_framework.permissions import (
    BasePermission,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from apps.api.models import Snippet
from apps.api.permissions import IsSnippetOwnerOrReadOnly
from apps.api.serializers import SnippetSerializer, UserSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset: BaseManager = Snippet.objects.all()
    serializer_class: type[SnippetSerializer] = SnippetSerializer
    permission_classes: list[type[BasePermission]] = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer: SnippetSerializer) -> None:
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset: BaseManager = Snippet.objects.all()
    serializer_class: type[SnippetSerializer] = SnippetSerializer
    permission_classes: list[type[BasePermission]] = [IsSnippetOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset: BaseManager = User.objects.all()
    serializer_class: type[UserSerializer] = UserSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset: BaseManager = User.objects.all()
    serializer_class: type[UserSerializer] = UserSerializer
    permission_classes: list[type[BasePermission]] = [IsAuthenticated]
