from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import *
from .serializers import *
# from .models import Category
# from .serializers import CategorySerializer
# Create your views here.

class CategoryView(viewsets.ViewSet):
    queryset = Category.objects.all()
    print(queryset)

    @extend_schema(responses= CategorySerializer)
    def list (self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
    


class ProductView(viewsets.ViewSet):
    queryset = Product.objects.all()


    @extend_schema(responses= ProductSerializer)
    def list (self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
    

class BrandView(viewsets.ViewSet):
    queryset = Brand.objects.all()
    print(queryset)

    @extend_schema(responses= BrandSerializer)
    def list (self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)