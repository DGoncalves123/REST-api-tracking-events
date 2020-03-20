from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
"""The other urls are all based on /api/

    See api.urls
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
]
