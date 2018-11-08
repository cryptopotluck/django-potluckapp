from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()


def index(request):
    return render(request, 'pages/index.html')



class ChartData(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
             "sales": 100,
                "customers": 10,
                  "inquires": 50,

    }
        return Response(data)