from django.shortcuts import get_object_or_404
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from ads.permissions import IsOwner, IsAdmin
from ads import serializers
from ads.models import Ad, Comment
from ads.filters import AdFilter


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def get_serializer_class(self):
        if self.action in ["list", "me"]:
            return serializers.AdSerializer
        return serializers.AdDetailSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    def get_permissions(self):
        permission_classes = (AllowAny,)
        if self.action not in ["retrieve", "list"]:
            permission_classes = (IsOwner | IsAdmin,)
        return tuple(permission() for permission in permission_classes)

    @action(detail=False, methods=["get"])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    def get_queryset(self):
        if self.action == "me":
            return self.queryset.filter(author=self.request.user).all()
        return self.queryset


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def perform_create(self, serializer):
        ad_id = self.kwargs.get("ad_pk")
        ad = get_object_or_404(Ad, id=ad_id)
        user = self.request.user
        serializer.save(author=user, ad=ad)

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Ad, id=ad_id)
        return ad_instance.comments.all()

    def get_permissions(self):
        permission_classes = (IsAuthenticated,)
        if self.action not in ["list", "retrieve"]:
            permission_classes = (IsOwner | IsAdmin,)
        return tuple(permission() for permission in permission_classes)
