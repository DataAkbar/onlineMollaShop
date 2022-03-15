from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ProductImage
# from cart.forms import CartAddProductForm


# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/index-13.html',
                  context={'category': category, 'categories': categories, 'products': products})


# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     return render(request, 'shop/product/product.html', context={'product': product})


def product_catalog(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/category.html',
                  context={'category': category, 'categories': categories, 'products': products})


def wishlist(request):
    return render(request, 'shop/product/wishlist.html')


def catigory_market(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/category-market.html',
                  context={'category': category, 'categories': categories, 'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    photos = ProductImage.objects.filter(product=product)
    # cart_product_form = CartAddProductForm()
    return render(request, 'shop/product.html',
                  context={'product': product, 'photos': photos})