from django.shortcuts import render

from rest_framework import viewsets,mixins
from rest_framework.permissions import AllowAny,IsAuthenticated

from situation.models import Occurrence
from situation.serializers import OccurrenceSerializer
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_gis.filters import DistanceToPointFilter



class SitViewSet(viewsets.ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    filter_backends = (DistanceToPointFilter, DjangoFilterBackend)
    filterset_fields = ['creator', 'category']
    distance_filter_field = 'location'
    

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'destroy' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]