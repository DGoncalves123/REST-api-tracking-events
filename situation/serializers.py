from rest_framework import serializers
from situation.models import Occurrence
from django.contrib.gis.geos import Point
from django.core.exceptions import ValidationError

class OccurrenceSerializer(serializers.HyperlinkedModelSerializer):
    
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
  
    class Meta:
        model = Occurrence
        fields = ('url','description','location','status','category','creator','update_date','status')
        read_only_fields = ['update_date']

    def create(self, validated_data):
        validated_data['status']=1
        Oc = Occurrence(**validated_data)
        Oc.save()
        return Oc

    def update(self, instance, validated_data):
        sta = validated_data.pop('status')
        instance.status = sta
        return instance

    def validate(self, data):

        if ('creator' in data):
            user=data['creator']
            if user.is_anonymous:
                raise ValidationError("Must be logged in to post occurrences.")
        
        if ('status' in data):
            if data['status']>3 or data['status']<1:
                raise ValidationError("Not a valid status value (1-to be validate, 2-validated, 3-resolved).")
        
        return data
