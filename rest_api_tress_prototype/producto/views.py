from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer
from django.http import *
# Create your views here.
class ListProduct(APIView):
	def get(self, request):
		productos = Producto.objects.all()
		producto_json = ProductoSerializer(productos, many=True)
		return Response(producto_json.data)

	def post(self, request):
		producto_json = ProductoSerializer(data = request.data)
		if producto_json.is_valid():
			producto_json.save()
			return Response(producto_json.data, status=201)
		return Response(producto_json.data.errors, status=400)

class DetailProduct(APIView):
	def get_object(self, pk):
		try:
			return Producto.objects.get(pk=pk)
		except Producto.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		producto = self.get_object(pk)
		producto_json = ProductoSerializer(producto)
		return Response(producto_json.data)
		

	def put(self, request, pk):
		producto = self.get_object(pk)
		producto_json = ProductoSerializer(producto, data=request.data)
		if producto_json.is_valid:
			producto_json.save()
			return Response(producto_json.data)
		return Response(producto_json.data.errors, status=400)
		
	def delete(self, request, pk):
		producto = self.get_object(pk)
		producto.delete()
		return Response(status=204)