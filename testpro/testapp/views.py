from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class TestAPIView(APIView):

    def get(self, request):
        response_data= {
            "message": "this is testing"
        }
        return Response(response_data, status=200)
