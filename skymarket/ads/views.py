from rest_framework import pagination, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from ads.permissions import IsOwner, IsAdmin
from ads import serializers
from ads.models import Ad


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination

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
            permission_classes = IsOwner | IsAdmin
        return tuple(permission() for permission in permission_classes)


class CommentViewSet(viewsets.ModelViewSet):
    pass
