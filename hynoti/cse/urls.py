from django.urls import include, path
from .views import CseNoticeListAPI, CseNoticeHaksaListAPI, CseNoticeEmploymentListAPI

urlpatterns = [
    path('', CseNoticeListAPI.as_view()),
    path('haksa/', CseNoticeHaksaListAPI.as_view()),
    path('employment/', CseNoticeEmploymentListAPI.as_view()),
]
