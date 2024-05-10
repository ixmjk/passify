from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Entry
from .serializers import (
    AddEntrySerializer,
    ListEntrySerializer,
    RetrieveEntrySerializer,
    UpdateEntrySerializer,
)


class EntryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = [
        "get",
        "post",
        "put",
        "patch",
        "delete",
        "head",
        "options",
    ]

    def get_queryset(self):
        return Entry.objects.filter(user_id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddEntrySerializer
        if self.request.method == "PUT":
            return UpdateEntrySerializer
        if self.request.method == "PATCH":
            return UpdateEntrySerializer
        if self.request.method == "GET":
            if self.action == "list":
                return ListEntrySerializer
            if self.action == "retrieve":
                return RetrieveEntrySerializer

    def get_serializer_context(self):
        return {"user_id": self.request.user.id, "request": self.request}
