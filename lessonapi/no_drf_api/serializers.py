from rest_framework import serializers

class PresentationSerializer(serializers.Serializer):
    deckId = serializers.IntegerField()
    authorUsername = serializers.CharField(max_length = 150)
    deckSlug = serializers.SlugField(max_length = 150)
