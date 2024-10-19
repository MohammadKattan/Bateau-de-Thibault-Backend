import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from mytig.config import baseUrl
from myRevendeurBackOffice.models import InfoProduct
from myRevendeurBackOffice.serializers import InfoProductSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django.http import JsonResponse
from django.views import View
import json
import os
# Create your views here.
class InfoProductList(APIView):
    #######################
#...TME3 JWT starts...#
#...end of TME3 JWT...#
#######################
    def get(self, request, format=None):
        products = InfoProduct.objects.all()
        serializer = InfoProductSerializer(products, many=True)
        return Response(serializer.data)


class InfoProductDetail(APIView):
    #######################
#...TME3 JWT starts...#
    # permission_classes = (IsAuthenticated,)
#...end of TME3 JWT...#
#######################
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, format=None):
        product = self.get_object(tig_id=tig_id)
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)
    

class putOnSale(APIView):
    #######################
#...TME3 JWT starts...#
    # permission_classes = (IsAuthenticated,)
#...end of TME3 JWT...#
#######################
    def get_object(self, tig_id,newPrice):
        try:
            product = InfoProduct.objects.get(tig_id=tig_id)
            product.sale = True
            product.discount = newPrice
            product.save() 
            return product
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id,newPrice,format=None):
        newPrice= float(newPrice)
        product = self.get_object(tig_id=tig_id,newPrice= newPrice)
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)
    
    
class removesale(APIView):
    #######################
#...TME3 JWT starts...#
    # permission_classes = (IsAuthenticated,)
#...end of TME3 JWT...#
#######################
    def get_object(self, tig_id):
        try:
            product = InfoProduct.objects.get(tig_id=tig_id)
            product.sale = False
            product.discount = 0
            product.save() 
            return product
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id,format=None):
        product = self.get_object(tig_id=tig_id)
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)
    
    
class incrementStock(APIView):
    def get_object(self, tig_id,addstock):
        try:
            product = InfoProduct.objects.get(tig_id=tig_id)
            product.sale = True
            product.quantityInStock += addstock
            product.save() 
            return product
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id,addstock,format=None):
        product = self.get_object(tig_id=tig_id , addstock= addstock)
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)
    
class decrementStock(APIView):
    def get_object(self, tig_id,lessstock):
        try:
            product = InfoProduct.objects.get(tig_id=tig_id)
            product.sale = True
            if (product.quantityInStock - lessstock)>=0:
                product.quantityInStock -= lessstock
            else: product.quantityInStock = 0
            product.save() 
            return product
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id,lessstock,format=None):
        product = self.get_object(tig_id=tig_id , lessstock= lessstock)
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)
    
class ReadJsonView(View):
    def get(self, request):
        file_path = os.path.join(os.path.dirname(__file__), '../../large_data_set_150.json')
        with open(file_path) as json_file:
            data = json.load(json_file)
        return JsonResponse(data,safe=False)