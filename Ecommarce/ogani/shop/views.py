from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog_details(request):
    return render(request, 'blog_details.html')

def blog(request):
    return render(request, 'blog.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def main(request):
    return render(request, 'main.html')

def shop_details(request):
    return render(request, 'shop_details.html')

def shop_grid(request):
    return render(request, 'shop_grid.html')

def shoping_cart(request):
    return render(request, 'shoping_cart.html')


def base(request):
    return render(request, 'base.html')