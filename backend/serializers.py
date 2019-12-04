from rest_framework import serializers


class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=0, )
    content = serializers.CharField(min_length=0, default='')
    exposed_sequence = serializers.IntegerField(default=0)
    url = serializers.CharField(min_length=0, default='')
    main_key_word = serializers.CharField(min_length=0, default='')
    reference = serializers.CharField(min_length=0, default='')
    written_date = serializers.CharField(min_length=0, default='')
    created_at = serializers.DateTimeField()
