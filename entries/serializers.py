from rest_framework import serializers

from .models import Entry


class ListEntrySerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedRelatedField(
        view_name="database-detail",
        read_only=True,
    )

    class Meta:
        model = Entry
        fields = ["id", "title", "username", "password", "url", "notes"]


class RetrieveEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ["id", "title", "username", "password", "url", "notes"]


class AddEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ["id", "title", "username", "password", "url", "notes"]

    def save(self, **kwargs):
        user_id = self.context["user_id"]
        self.instance = Entry.objects.create(user_id=user_id, **self.validated_data)
        return self.instance


class UpdateEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = [
            "title",
            "username",
            "password",
            "url",
            "notes",
        ]
