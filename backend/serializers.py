from rest_framework import serializers

from backend.models import News


class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100000)
    content = serializers.CharField(max_length=100000, default='')
    exposed_sequence = serializers.IntegerField(default=0)
    url = serializers.CharField(max_length=100000, default='')
    main_key_word = serializers.CharField(max_length=100000, default='')
    reference = serializers.CharField(max_length=100000, default='')
    written_date = serializers.CharField(max_length=100000, default='')
    created_at = serializers.DateTimeField()
