from rest_framework import serializers
from .models import PortalNotice


class PortalNoticeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PortalNotice
        fields = '__all__'