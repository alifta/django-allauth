from rest_framework import serializers

from core.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Todo
        fields = ["id", "user", "description", "is_completed", "created_at", "updated_at"]
        read_only_fields = ["id", "user", "created_at", "updated_at"]
