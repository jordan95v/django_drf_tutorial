from rest_framework import serializers
from apps.api.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model: type[Snippet] = Snippet
        fields: list[str] = [
            "id",
            "title",
            "language",
            "code",
            "owner",
            "created_at",
            "updated_at",
        ]


class UserSerializer(serializers.ModelSerializer):
    snippet_count = serializers.SerializerMethodField()

    def get_snippet_count(self, obj: User) -> int:
        return obj.snippets.count()

    class Meta:
        model: type[User] = User
        exclude: list[str] = []
