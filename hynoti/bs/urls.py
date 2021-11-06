from django.urls import include, path
from .views import (BsNoticeListAPI, BsNoticeClassListAPI, BsNoticeGradeListAPI, 
    BsNoticeGraduationListAPI, BsNoticeMajorListAPI)

urlpatterns = [
    path('', BsNoticeListAPI.as_view()),
    path('class/', BsNoticeClassListAPI.as_view()),
    path('grade/', BsNoticeGradeListAPI.as_view()),
    path('graduation/', BsNoticeGraduationListAPI.as_view()),
    path('major/', BsNoticeMajorListAPI.as_view()),
]