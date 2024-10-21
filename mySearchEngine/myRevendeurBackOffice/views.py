import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from mytig.config import baseUrl
from myRevendeurBackOffice.models import InfoProduct
from myRevendeurBackOffice.serializers import InfoProductSerializer
from myRevendeurBackOffice.models import ProduitPoisson
from myRevendeurBackOffice.serializers import ProduitPoissonSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django.http import JsonResponse
from django.views import View
import json
import os
# Create your views here.
class InfoProductList(APIView):
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
    
    
class updatePrice(APIView):
    def get_object(self, tig_id,newPrice):
        try:
            product = InfoProduct.objects.get(tig_id=tig_id)
            product.price = newPrice
            product.save() 
            return product
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id,newPrice,format=None):
        product = self.get_object(tig_id=tig_id , newPrice= newPrice)
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)
    
class ReadJsonView(View):
    def get(self, request):
        file_path = os.path.join(os.path.dirname(__file__), '../../large_data_set_150.json')
        with open(file_path) as json_file:
            data = json.load(json_file)
        return JsonResponse(data,safe=False)
    
class PoissonsList(APIView):
    def get(self, request, format=None):
        print("test test")
        res=[]
        for prod in ProduitPoisson.objects.all():
            serializer = ProduitPoissonSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            print(jsondata)
        return JsonResponse(res, safe=False)
    
from django.views import View
from django.http import JsonResponse
import json
import os
from datetime import datetime

from django.views import View
from django.http import JsonResponse
import json
import os
from datetime import datetime

class newOperation(APIView):
    def get(self, request, category, type, stock, priceOperation):
        is_achat = type.lower() == 'true'
        category_mapping = {
            0: "Poisson",
            1: "Coquillage",
            2: "Crustacé"
        }
        categoryName = category_mapping.get(int(category), "Inconnu")
        print("test test from views")
        file_path = os.path.join(os.path.dirname(__file__), '../../large_data_set_150.json')
        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = []
        new_data = {
            "pid": max([item['pid'] for item in data], default=0) + 1,
            "category": int(category),
            "category_name": categoryName,
            "price": float(priceOperation), 
            "quantity": int(stock),  
            "date": datetime.now().strftime("%Y-%m-%d"), 
            "achat": is_achat,  
            "type_promotion": None, 
            "discount": 0.0,
            "total_invoice": int(stock) * float(priceOperation)
        }
        data.append(new_data)
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return JsonResponse({"message": "Nouvelle donnée ajoutée avec succès!", "pid": new_data["pid"]}, status=201)

