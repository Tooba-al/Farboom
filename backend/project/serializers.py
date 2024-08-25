from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Project, ProjectAttachment


class ProjectAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAttachment
        fields = ('id', 'get_image',)


class ProjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    attachments = ProjectAttachmentSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ('id', 'content', 'title', 'address','created_by', 'created_at_formatted', 'attachments')


class ProjectDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    attachments = ProjectAttachmentSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ('id', 'content', 'title', 'address', 'created_by', 'created_at_formatted', 'attachments',)