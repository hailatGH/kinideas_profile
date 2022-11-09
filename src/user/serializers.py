from dataclasses import fields
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import *

class UserPrivilegeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPrivilegeModel
        fields = '__all__'

class SubscribedUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscribedUsersModel
        fields = '__all__'

class NoOfSkipsSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoOfSkipsModel
        fields = '__all__'