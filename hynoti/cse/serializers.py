from rest_framework import serializers
from .models import CseNotice


class CseNoticeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CseNotice
        fields = '__all__'