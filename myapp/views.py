from django.shortcuts import render,redirect

from .models import student

from .forms import studentform

# Create your views here.
def Home(request):
    Student=student.objects.all

    form=studentform
    return render(request,'Home.html',{'form':form,'Student':Student})
def add(request):
    form=studentform(request.POST)
    form.save()
    return redirect('/')

def edit(request,id):
    Student=student.objects.get(id=id)

    return render(request,'edit.html',{'Student':Student})

def update(request,id):
    Student=student.objects.get(id=id)
    form=studentform(request.POST,instance=Student)
    form.save()

    return redirect('/')

def delete(request,id):
    Student=student.objects.get(id=id)
    Student.delete()
    return redirect('/')
