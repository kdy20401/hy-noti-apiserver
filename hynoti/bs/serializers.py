from rest_framework import serializers
from .models import BsNotice


class BsNoticeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BsNotice
        fields = '__all__'