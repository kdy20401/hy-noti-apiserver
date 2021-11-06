from rest_framework import generics
from rest_framework import mixins
from .serializers import PortalNoticeSerializer
from .models import PortalNotice
from django.views.generic import ListView


class PortalNoticeListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = PortalNoticeSerializer

    def get_queryset(self):
        return PortalNotice.objects.all().order_by('-date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PortalNoticeHaksaListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = PortalNoticeSerializer

    def get_queryset(self):
        return PortalNotice.objects.filter(category='학사')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
class PortalNoticeAdmissionListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = PortalNoticeSerializer

    def get_queryset(self):
        return PortalNotice.objects.filter(category='입학')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
class PortalNoticeEmploymentListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = PortalNoticeSerializer

    def get_queryset(self):
        return PortalNotice.objects.filter(category='취업')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
class PortalNoticeStartupListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = PortalNoticeSerializer

    def get_queryset(self):
        return PortalNotice.objects.filter(category='창업')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
class PortalNoticeRecruitListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = PortalNoticeSerializer

    def get_queryset(self):
        return PortalNotice.objects.filter(category='모집채용')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
class PortalNoticeGyeongjosaListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = PortalNoticeSerializer

    def get_queryset(self):
        return PortalNotice.objects.filter(category='경조사')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
class PortalNoticeNormalListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = PortalNoticeSerializer

    def get_queryset(self):
        return PortalNotice.objects.filter(category='일반')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
class PortalNoticeResearchListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = PortalNoticeSerializer

    def get_queryset(self):
        return PortalNotice.objects.filter(category='산학연구')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
class PortalNoticeScholarshipListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = PortalNoticeSerializer

    def get_queryset(self):
        return PortalNotice.objects.filter(category='장학')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PortalNoticeEventListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = PortalNoticeSerializer

    def get_queryset(self):
        return PortalNotice.objects.filter(category='행사안내')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
# class PortalNoticeDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
#     serializer_class = PortalNoticeSerializer

#     def get_queryset(self):
#         return PortalNotice.objects.all().order_by('id')

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class PortalNoticeList(ListView):
#     model = PortalNotice
#     template_name = 'portal.html'
#     context_object_name = 'portal_notices'
