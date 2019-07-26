from rest_framework import serializers
from api.models import RouteChange

class RouteChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteChange
        fields = '__all__'
