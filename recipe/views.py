from django.shortcuts import render
from .models import Menu
from rest_framework import generics, status
from .serializer import MenuSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


class MenuView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class GetMenu(APIView):
    serializer_calss = MenuSerializer
    lookup_url_kwarg = 'menu_name'

    def get(self, request, menu_name, format=None):
        if menu_name != None:
            menu = Menu.objects.filter(name=menu_name)
            if len(menu) > 0:
                data = MenuSerializer(menu[0]).data
                return Response(data, status=status.HTTP_200_OK)
            return Response({'Meny Not Found': 'Invalid Menu Name'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Bad Request': 'Name parameter not found in request'}, status=status.HTTP_400_BAD_REQUEST)
