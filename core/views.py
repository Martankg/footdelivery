from unicodedata import category
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from core.models import FoodCard, Category
# Create your views here.
def base(request):
    categories = Category.objects.all() 
    foodCards = FoodCard.objects.all()
    context = {'foodCards':foodCards, 'categories':categories}
    return render(request, 'index.html', context=context)


# def test(request, id):
#     categories = Category.objects.all()
#     category = Category.objects.get(id=id)
#     # category1 = FoodCard.objects.all().filter(category=title)
#     print(categories)
#     return render(request, 'index.html', {'categories':categories, 'category':category})

def product(request, id):
    foodcard = FoodCard.objects.get(id=id)
    one_type_categories = FoodCard.objects.all().filter(category=foodcard.category)
    return render(request, 'product.html', {'foodcard':foodcard, 'one_type_categories':one_type_categories})
cart_products =[]
def addCart(request, pk):
    cart_session = request.session.get('cart_session', [])
    cart_products.append(pk)
    print(cart_products)
    return HttpResponseRedirect('/')

def cart(request):
    return render(request, 'cart.html')