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
        fields = (
            "pk",
            "text",
            "created_at",
            "author_id",
            "ad_id",
            "author_first_name",
            "author_last_name",
            "author_image",
        )


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "description")


class AdDetailSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.id")
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    phone = serializerfields.PhoneNumberField(source="author.phone", read_only=True)

    class Meta:
        model = Ad
        fields = (
            "pk",
            "image",
            "title",
            "price",
            "author_first_name",
            "author_last_name",
            "description",
            "author_id",
            "phone",
        )
