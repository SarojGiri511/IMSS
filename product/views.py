from django.shortcuts import render
from .models import product

# Create your views here.
def productHome(request):
    context = {
        'title':'products',
        'products':product.objects.all() #TO get all data from product table
    }
    return render(request,'index.html', context)

def productdetail(request):
    return render(request, 'detail.html')