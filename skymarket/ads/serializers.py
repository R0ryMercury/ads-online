from phonenumber_field import serializerfields
from rest_framework import serializers
from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.id")
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    ad_id = serializers.ReadOnlyField(source="ad.id")
    author_image = serializers.ImageField(required=False)

    class Meta:
        model = Comment
        exclude = ["ad", "author"]


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        exclude = ["created_at", "author"]


class AdDetailSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.id")
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")

    class Meta:
        model = Ad
        exclude = ["author"]
