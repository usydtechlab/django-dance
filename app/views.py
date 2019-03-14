#from django.shortcuts import render
from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


def index(request):
    permission_classes = (IsAuthenticated,)
    return HttpResponse('Hello, World!')

class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    #queryset = Songs.objects.all()
    #serializer_class = SongsSerializer

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
