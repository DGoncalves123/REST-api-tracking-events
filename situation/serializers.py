from rest_framework import serializers
from situation.models import Occurrence
from django.contrib.gis.geos import Point
from django.core.exceptions import ValidationError

class OccurrenceSerializer(serializers.HyperlinkedModelSerializer):
    #creator = serializers.SerializerMethodField('_user')

    #def _user(self, obj):
    #    request = getattr(self.context, 'request', None)
    #    if request:
    #        return request.user
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    #status = serializers.HiddenField(default=1)
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

    #    instance.email = validated_data.get('email', instance.email)
    #    instance.save()

    #    extra.first_name = extra_data.get('first_name', extra.first_name)
    #    extra.last_name = extra_data.get('last_name', extra.last_name)
    #    extra.save()

        return instance

    def validate(self, data):
        """
        Must check location format before you can put it into an object
        """
        if ('location' in data):
            split=data['location'].split(' ')
            if len(split)==2:
                try:
                    lat=float(split[0])
                    lon=float(split[1])
                except:
                    raise ValidationError("Wrong format for location, must match: \'latitude longitude\'.")
            else:
                raise ValidationError("Wrong format for location, must match: \'latitude longitude\'.")
            if lat>90 or lat<-90 or lon>180 or lon<-180:
                raise ValidationError("Wrong format for location, must be a real coordinate.")
            p=Point(lat,lon)
            data['location']=p

        if ('creator' in data):
            user=data['creator']
            if user.is_anonymous:
                raise ValidationError("Must be logged in to post occurrences.")
        print()
        print(list(data.keys()))
        print()
        if ('status' in data):
            if data['status']>3 or data['status']<1:
                raise ValidationError("Not a valid status value (1-to be validate, 2-validated, 3-resolved).")
        
        return data
