from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def cart(request):
    return render(request,'carrinho.html')

def price(request):
    return render(request,'produtos.html')