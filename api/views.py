from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api.serializers import TodoSerializer
from core.models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing todos.
    Users can only view and manage their own todos.
    """

    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Return todos for the current user only."""
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Set the user field to the current user when creating a todo."""
        serializer.save(user=self.request.user)


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def get_token_from_session(request):
    """
    Convert Django session authentication to JWT token.
    This allows users who are already logged in via allauth to get API tokens.
    """
    user = request.user
    refresh = RefreshToken.for_user(user)

    return Response(
        {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "username": user.username,
        },
        status=status.HTTP_200_OK,
    )
