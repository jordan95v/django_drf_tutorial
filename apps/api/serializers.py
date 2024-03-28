from rest_framework import serializers
from apps.api.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model: type[Snippet] = Snippet
        fields: list[str] = [
            "id",
            "title",
            "language",
            "code",
            "created_at",
            "updated_at",
        ]
