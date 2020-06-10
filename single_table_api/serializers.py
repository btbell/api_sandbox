from rest_framework import serializers
from .models import MediaMention

class MediaMentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaMention
        fields = (
            'publication_date',
            'attribution_type',
            'last_name',
            'andrew_id',
            'category',
            'publication',
            'title',
            'article_link'
        )