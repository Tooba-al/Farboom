from rest_framework import serializers

from account.serializers import UserSerializer

from .models import News, NewsAttachment


class NewsAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsAttachment
        fields = ('id', 'get_image',)


class NewsSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    attachments = NewsAttachmentSerializer(read_only=True, many=True)

    class Meta:
        model = News
        fields = ('id', 'content', 'title', 'address','created_by', 'created_at_formatted', 'attachments')


class NewsDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    attachments = NewsAttachmentSerializer(read_only=True, many=True)

    class Meta:
        model = News
        fields = ('id', 'content', 'title', 'address', 'created_by', 'created_at_formatted', 'attachments',)