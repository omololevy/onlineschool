from rest_framework import serializers
from .models import (Sinflar, Mavzular, Fanlar, Amaliyot, Maruza)

class SinfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sinflar
        fields = "__all__"

class FanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fanlar
        fields = "__all__"

class MavzuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mavzular
        fields = "__all__"

class MaruzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maruza
        fields = "__all__"

class AmaliyotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amaliyot
        fields = "__all__"
