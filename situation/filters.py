import django_filters 
from rest_framework_gis import filters
from rest_framework_gis.filters import DistanceToPointFilter

from .models import Occurrence

class IntersectionFilter(GeoFilterSet):
    slug_name = django_filters.CharFilter(name='slug_name', lookup_type='exact')
    geometry = filters.GeometryFilter(name='geometry', lookup_type='intersects')

    filter_overrides = {}

    class Meta:
        model = GeoData