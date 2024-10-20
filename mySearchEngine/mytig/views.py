import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from mytig.config import baseUrl

# Create your views here.
class RedirectionListeDeProduits(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        return Response(jsondata)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class RedirectionDetailProduit(APIView):
    def get(self, request, pk, format=None):
        try:
            response = requests.get(baseUrl+'product/'+str(pk)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"



from mytig.models import ProduitEnPromotion
from mytig.models import ProduitAvailable
from mytig.models import ProduitPoisson
from mytig.serializers import ProduitEnPromotionSerializer
from mytig.serializers import ProduitAvailableSerializer
from mytig.serializers import ProduitPoissonSerializer
from django.http import Http404
from django.http import JsonResponse

class PromoList(APIView):
    def get(self, request, format=None):
        res=[]
        print(ProduitEnPromotion.objects.all())
        for prod in ProduitEnPromotion.objects.all():
            serializer = ProduitEnPromotionSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class PromoDetail(APIView):
    def get_object(self, pk):
        try:
            return ProduitEnPromotion.objects.get(pk=pk)
        except ProduitEnPromotion.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProduitEnPromotionSerializer(prod)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"


class RedirectionListeDeShipPoints(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'shipPoints/')
        jsondata = response.json()
        return Response(jsondata)
    
    
class RedirectionDetailShipPoint(APIView):
    def get(self, request, pk, format=None):
        try:
            response = requests.get(baseUrl+'shipPoint/'+str(pk)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404
        
class AvailableList(APIView):
    def get(self, request, format=None):
        res=[]
        for prod in ProduitAvailable.objects.all():
            serializer = ProduitAvailableSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
    
    
class AvailableDetail(APIView):
    def get_object(self, pk):
        try:
            return ProduitAvailable.objects.get(pk=pk)
        except ProduitAvailable.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProduitAvailableSerializer(prod)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)

class PoissonsList(APIView):
    def get(self, request, format=None):
        res=[]
        for prod in ProduitPoisson.objects.all():
            serializer = ProduitPoissonSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
    