from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.filters import SearchFilter


from myapp.serializers import LoginSerializer, OrganizationSerializer
# Create your views here.
# def TenantView(request):
    
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['name']
    

class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={"request":request})
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.validated_data["user"]
        
        # generate JWT Tokens
        refresh =  RefreshToken.for_user(user)
        
        return Response({
            "access":str(refresh.access_token),
            "refresh": str(refresh),
            "user":{
                "id":user.id,
                "username":user.username,
                "email":user.email,
            }
        }, status=status.HTTP_200_OK)