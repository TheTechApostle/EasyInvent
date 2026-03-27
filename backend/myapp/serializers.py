from rest_framework import serializers
from .models import * 
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Organization
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['id', 'name', 'created_at']
        

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )
    
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        
        if not username or not password:
            raise serializers.ValidationError('Both Username and Password Required')

        
        user = authenticate(
            request=self.context.get("request"),
            username=username,
            password=password,
        )        
        
        
        if not user:
            raise serializers.ValidationError('Invalid Credential or The account has  be deactivated')
        
        attrs["user"] =  user
        return attrs
        
