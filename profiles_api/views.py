from email import message
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from profiles_api import serializers
from django.shortcuts import render

from .models import Hypervisortabledb
from .serializers import HypervisortabledbSerializer

class HypervisorConnect(APIView):
    """Get the Hypervisor information class"""

    def get(self, request):
        hypervisorInfo = Hypervisortabledb.objects.filter(hypervisorIP = "192.168.150.17")
        serializer = HypervisortabledbSerializer(hypervisorInfo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        if request.method == 'POST':
            username = request.POST["user"]
            password = request.POST["pass"]
            ipaddress = request.POST["ipaddr"]
      
        dict = {
            'username': username,
            'password': password,
            'ipaddress': ipaddress
        }
        
        
        return render(request, 'index.html', dict)
        

def dashboard(request):
    return render(request, "index.html")
    
