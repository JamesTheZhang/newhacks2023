from rest_framework import serializers
from .models import *

class UserProfileFriendSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = UserProfile
        fields=('cur_longitude', 'cur_latitude')

class UserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    friend = UserProfileFriendSerializer(read_only=True, many=True)

    class Meta:
        model = UserProfile
        fields = ('cur_longitude', 'cur_latitude', 'profile_picture')
