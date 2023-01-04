from rest_framework import pagination, viewsets
from ads import serializers
from ads.models import Ad


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.AdSerializer
        return serializers.AdDetailSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    

class CommentViewSet(viewsets.ModelViewSet):
    pass
