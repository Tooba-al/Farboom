from rest_framework import serializers

from account.serializers import UserSerializer

from .models import *


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'email', 'age', 'education', 'cv', 'created_at_formatted',)


# class ResumetDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Resume
#         fields = ('id', 'first_name', 'last_name', 'phone_number', 'age', 'education', 'cv', 'created_at_formatted',)
