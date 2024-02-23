from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def inventoryHome(request):

    return HttpResponse('I am going to support inventory')