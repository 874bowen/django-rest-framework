from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializerRequest(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']


class SnippetSerializerResponse(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['title', 'code', 'language']