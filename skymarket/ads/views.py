from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from ads.permissions import IsOwner, IsAdmin
from ads import serializers
from ads.models import Ad
from ads.filters import AdFilter


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    permission_classes = (AllowAny,)
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
        if self.action == "retrieve":
            permission_classes = (AllowAny,)
        elif self.action != "list":
            permission_classes = (IsOwner | IsAdmin,)
        return tuple(permission() for permission in permission_classes)

    @action(detail=False, methods=["get"])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user).all()
        return self.queryset


class CommentViewSet(viewsets.ModelViewSet):
    pass
