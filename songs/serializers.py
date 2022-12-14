from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "album_id", "duration", "title"]
        read_only_fields = ["album_id"]
