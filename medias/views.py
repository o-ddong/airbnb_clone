from django.shortcuts import render
from rest_framework.views import APIView

from .models import Photo

# Create your views here.
class PhotoDetail(APIView):
    def get_objects(pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            

    def delete(self, request, pk):
        pass
