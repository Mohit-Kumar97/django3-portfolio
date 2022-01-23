from django.shortcuts import render
from .models import Portfoliomodel

def home(request):
    projects=Portfoliomodel.objects.all()
    return render(request,'projectsfolio/home.html',{'projects':projects})
