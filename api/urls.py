from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet
"""Situation urls to be after /api/ 

Due to it still being part of the 'api'   
"""


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^', include('situation.urls')),
]