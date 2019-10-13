from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import QueryDict


from .models import Product


# GET PRODUCT -- GET METHOD
@csrf_exempt
def getproducts(request):
    if request.method == 'GET':
        product_list = list(Product.objects.values())
        return JsonResponse(dict(products=product_list), safe=False)


# ADD PRODUCT -- POST METHOD
@csrf_exempt
def addproduct(request):
    if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('description') and request.POST.get('price'):
                product=Product()
                product.name= request.POST.get('name')
                product.description= request.POST.get('description')
                product.price = request.POST.get('price')
                product.save()

                data = dict()
                data['name'] = product.name
                data['description'] = product.description
                data['price'] = product.price
                data['id'] = product.id
                return JsonResponse(data, safe=False)
                # RETURN THE ONE PRODUCT TO BE ADDED ON FRONT END TABLE


# UPDATE PRODUCT -- UPDATE REQUEST BODY
@csrf_exempt
def updateproduct(request):

    data = QueryDict(request.body)
    existing = data['id']
    name = data['name']
    description = data['description']
    price = data['price']

    if request.method == 'PUT':

            product=Product()
            product = Product.objects.get(id=existing)

            product.name = name
            product.description = description
            product.price = price
            product.save()

            print(product.id)

            data = dict()
            data['name'] = name
            data['description'] = description
            data['price'] = price
            data['id'] = product.id


            return JsonResponse(data, safe=False)


# DELETE PRODUCT -- DELETE METHOD
@csrf_exempt
def deleteproduct(request):
    if request.method == 'DELETE':
        deletedata = QueryDict(request.body)
        id = deletedata['id']

        product = Product.objects.get(id=id)
        product.delete()

        data = dict()
        data['id'] = id
        return JsonResponse(data, safe=False)
