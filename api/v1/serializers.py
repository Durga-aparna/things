from rest_framework import serializers
from buses.models import bus
class carSerializer(serializers.ModelSerializer):
    class Meta:
        model=bus
        fields="__all__"