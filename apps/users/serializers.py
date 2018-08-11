from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from apps.users.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserProfile
        fields='__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=UserProfile.objects.all(),
                fields=('name'),
                # message的信息可以自定义
                message="已经收藏"
            )
        ]