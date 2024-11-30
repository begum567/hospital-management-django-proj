from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm
from .models import Departments,Doctors

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        
    form= BookingForm()
    dict_form={
        'form':form
    }
    
    return render(request,'booking.html',dict_form)


def contact(request):
    return render(request,'contact.html')


def doctors(request):
    
    dict_doc={
        'doct':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doc)

def department(request):
    
    dict_dept={
        'dept':Departments.objects.all()
        
    }
    return render(request,'department.html',dict_dept)