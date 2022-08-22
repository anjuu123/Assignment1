from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from.models import Student, Department

# Create your views here.
def index(request):  
    return render(request, "index.html")


def student(request):
    
    mydetails = Student.objects.all().values()
    template=loader.get_template("student.html")
    context={
    "mydetails": mydetails,
    }
    
    return HttpResponse(template.render(context,request))

# def addstudent(request):
    
#     f = request.POST('firstname'),
#     l = request.POST('lastname'),
#     d = request.POST('dob'),
#     r = request.POST('roll'),
#     dp = request.POST('dpname'),
#     cn = request.POST('course'),
#     s = request.POST('semester')

#     student = Student(firstname=f, lastname=l, dateofbirth = d, rollno = r, deptname = dp, coursename = cn, semester = s)
#     student.save()
#     return HttpResponseRedirect(reverse("student.html"))   

def dept(request):

    mydept= Department.objects.all().values()
    template=loader.get_template("dept.html")
    context={
    "mydept": mydept,
    }

    return HttpResponse(template.render(context,request))
