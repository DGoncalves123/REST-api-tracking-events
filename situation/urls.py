from django.conf.urls import url, include
from rest_framework import routers
from situation.views import SitViewSet

router = routers.DefaultRouter()
router.register(r'situation', SitViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]