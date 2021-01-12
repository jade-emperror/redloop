from django.shortcuts import render
from django.http import HttpResponse
from .models import jobs

# Create your views here.
def career(request):
    careers=jobs.objects.all()
    return render(request,'career.html',{'careers':careers})