from django.shortcuts import render, get_object_or_404
from .models import Project
from django.http import HttpResponse

# Create your views here.

def base(request):
    projects = Project.objects.all()
    return render(request,'mypage/base.html',{'projects': projects})

def detail(request,slug):
    project = get_object_or_404(Project,slug=slug)
    return render(request,'mypage/detail.html',{'project':project})
    # return HttpResponse("You're looking at project %s." % project)
    