from rest_framework import serializers
from .models import Presentation


class PresentationSerializer(serializers.Serializer):
    deckId = serializers.IntegerField(required = False)
    authorUsername = serializers.CharField(max_length = 150)
    deckSlug = serializers.SlugField(max_length = 150)

    def create(self, validated_data):
        return Presentation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.deckId = validated_data.get('deckId', instance.deckId)
        instance.authorUsername = validated_data.get('authorUsername',
                                                     instance.authorUsername)
        instance.deckSlug = validated_data.get('deckSlug', instance.deckSlug)
        instance.save()
        return instance


class PresentationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = ['deckId', 'authorUsername', 'deckSlug']
