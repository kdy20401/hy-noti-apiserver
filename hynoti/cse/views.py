from rest_framework import generics
from rest_framework import mixins
from .serializers import CseNoticeSerializer
from .models import CseNotice
from django.views.generic import ListView


class CseNoticeListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = CseNoticeSerializer

    def get_queryset(self):
        return CseNotice.objects.all().order_by('-date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CseNoticeHaksaListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = CseNoticeSerializer

    def get_queryset(self):
        return CseNotice.objects.filter(category='학사일반')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CseNoticeEmploymentListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = CseNoticeSerializer

    def get_queryset(self):
        return CseNotice.objects.filter(category='취업정보')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)