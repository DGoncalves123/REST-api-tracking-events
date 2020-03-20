from rest_framework import serializers
from api.models import UserBase, User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UserBaseSerializer(serializers.HyperlinkedModelSerializer):
    extra = UserSerializer(required=True)

    class Meta:
        model = UserBase
        fields = ('url','email','password','extra')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        extra_data = validated_data.pop('extra')
        password = validated_data.pop('password')
        user = UserBase(**validated_data)
        user.set_password(password)
        user.save()
        User.objects.create(user=user, **extra_data)
        return user

    def update(self, instance, validated_data):
        extra_data = validated_data.pop('extra')
        extra = instance.extra

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        extra.first_name = extra_data.get('first_name', extra.first_name)
        extra.last_name = extra_data.get('last_name', extra.last_name)
        extra.save()

        return instance

