from rest_framework import generics
from rest_framework import mixins
from .serializers import BsNoticeSerializer
from .models import BsNotice
from django.views.generic import ListView


class BsNoticeListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = BsNoticeSerializer

    def get_queryset(self):
        return BsNotice.objects.all().order_by('-date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BsNoticeClassListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = BsNoticeSerializer

    def get_queryset(self):
        return BsNotice.objects.filter(category='수업')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BsNoticeGradeListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = BsNoticeSerializer

    def get_queryset(self):
        return BsNotice.objects.filter(category='성적')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BsNoticeGraduationListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = BsNoticeSerializer

    def get_queryset(self):
        return BsNotice.objects.filter(category='졸업')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BsNoticeMajorListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = BsNoticeSerializer

    def get_queryset(self):
        return BsNotice.objects.filter(category='전공')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)