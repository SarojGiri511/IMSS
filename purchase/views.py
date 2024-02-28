from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def purchasedetail(request):
    return render(request, 'home.html')