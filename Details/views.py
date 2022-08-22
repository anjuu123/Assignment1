from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from.models import Student, Department

# Create your views here.

def index(request):
    mydetails = Student.objects.all().values()
    template=loader.get_template("index.html")
    context={
    "mydetails": mydetails,
    }
    return HttpResponse(template.render(context,request))