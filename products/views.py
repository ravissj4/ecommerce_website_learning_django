from django.shortcuts import render, Http404
from .models import Product, ProductImage

# # Create your views here.
# def home(request):
#     # context = locals()
#     if request.user.is_authenticated():
#         # username_is = "Ravi Ranjan"
#         # context = {'username_is' : username_is}
#         context = {'username_is' : request.user}
#     else:
#         context = {'username_is' : request.user}
    
#     template = 'products/home.html'
    

#     return render(request, template, context)

def home(request):
    products = Product.objects.all()
    template = 'products/home.html'
    context = {"products" : products}
    return render(request, template, context)

def all(request):
    products = Product.objects.all()
    template = 'products/all.html'
    context = {"products" : products}
    return render(request, template, context)

# def single(request, slug):
# def single(request, id):
def single(request, slug):
    try:
        # print(slug)
        # product = Product.objects.get(id=id)
        product = Product.objects.get(slug=slug)
        # images = Product.productimage_set.all()
        images = ProductImage.objects.filter(product=product)
        template = 'products/single.html'
        context = {"product" : product, "images": images}
        return render(request, template, context)
    except:
        raise Http404