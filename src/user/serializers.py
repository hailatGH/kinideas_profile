from dataclasses import fields
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import *

class UserPrivilegeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPrivilegeModel
        fields = '__all__'