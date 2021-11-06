from rest_framework import permissions
from django.conf import settings


class SafelistPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        remote_addr = request.META['REMOTE_ADDR']

        for ip in settings.REST_SAFE_IP_LIST:
            if remote_addr == ip:
                return True

        return False