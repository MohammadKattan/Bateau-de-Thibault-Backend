from django import forms
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
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django import forms

class CreateAdminUserView(View):
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        admin_user = User.objects.create_user(username=username, email=email, password=password)
        admin_user.first_name = first_name
        admin_user.last_name = last_name
        admin_user.is_staff = True  
        admin_user.is_superuser = True  
        admin_user.save()
        return JsonResponse({'message': 'Utilisateur admin créé avec succès!'})

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])  
        if commit:
            user.save()
        return user
    

class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  
        return render(request, 'registration/register.html', {'form': form})



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
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, '../large_data_set_150.json')
        if not os.path.exists(file_path):
            return JsonResponse({'error': 'File not found'}, status=404)
        with open(file_path) as json_file:
            data = json.load(json_file)
        return JsonResponse(data, safe=False)