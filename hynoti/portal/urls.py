from django.urls import include, path
from .views import (PortalNoticeListAPI, PortalNoticeHaksaListAPI, PortalNoticeAdmissionListAPI,
    PortalNoticeEmploymentListAPI, PortalNoticeStartupListAPI, PortalNoticeRecruitListAPI,
    PortalNoticeGyeongjosaListAPI, PortalNoticeNormalListAPI, PortalNoticeResearchListAPI, 
    PortalNoticeScholarshipListAPI, PortalNoticeEventListAPI)

urlpatterns = [
    #path('api-auth/', include('rest_framework.urls')),
    path('', PortalNoticeListAPI.as_view()),
    path('haksa/', PortalNoticeHaksaListAPI.as_view()),
    path('admission/', PortalNoticeAdmissionListAPI.as_view()),
    path('employment/', PortalNoticeEmploymentListAPI.as_view()),
    path('startup/', PortalNoticeStartupListAPI.as_view()),
    path('recruit/', PortalNoticeRecruitListAPI.as_view()),
    path('gyeongjosa/', PortalNoticeGyeongjosaListAPI.as_view()),
    path('normal/', PortalNoticeNormalListAPI.as_view()),
    path('research/', PortalNoticeResearchListAPI.as_view()),
    path('scholarship/', PortalNoticeScholarshipListAPI.as_view()),
    path('event/', PortalNoticeEventListAPI.as_view())
]
