from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def likith(request):
    return render(request,'likith.html')