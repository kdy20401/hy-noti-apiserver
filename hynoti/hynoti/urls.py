from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('notice/portal/', include('portal.urls')),
    path('notice/cse/', include('cse.urls')),
    path('notice/bs/', include('bs.urls')),
]