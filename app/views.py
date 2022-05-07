from logging import exception
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == "POST":
        customer=Ludi()
        customer.name = request.POST.get('name')
        customer.phone = request.POST.get('number')
        customer.email = request.POST.get('email')
        customer.letter = request.POST.get('message')
        customer.cource1 = request.POST.get('front')
        customer.cource2 = request.POST.get('backend')
        customer.cource3 = request.POST.get('ux')
        customer.cource4 = request.POST.get('step')
        customer.save()

    return render(request, 'inc/index.html')

def contact(request):
    if request.method == "POST":
        customer=Clients()
        customer.name = request.POST.get('name')
        customer.phone = request.POST.get('number')
        customer.email = request.POST.get('email')
        customer.letter = request.POST.get('message')
        customer.cource1 = request.POST.get('front')
        customer.cource2 = request.POST.get('backend')
        customer.cource3 = request.POST.get('ux')
        customer.cource4 = request.POST.get('step')
        customer.save()
    return render(request, 'inc/contact-us.html')

def cource(request):
    if request.method == "POST":
        customer=Clients()
        customer.name = request.POST.get('name')
        customer.phone = request.POST.get('number')
        customer.email = request.POST.get('email')
        customer.letter = request.POST.get('message')
        customer.cource1 = request.POST.get('front')
        customer.cource2 = request.POST.get('backend')
        customer.cource3 = request.POST.get('ux')
        customer.cource4 = request.POST.get('step')
        customer.save()
    return render(request, 'inc/cource.html')

def about_us(request):
    sod = Workers.objects.all()
    name = sod.values('f_name')
    post = sod.values('post')
    d = sod.values('discription')
    link1 = sod.values('link1')
    contact = sod.values('contact')
    context = {
        'name':name,
        'post':post,
        'd':d,
        'link1':link1,
        'contact':contact,
        'all':sod,
    }   
    return render(request, 'inc/about_us.html', context)

def service(request):
    return render(request, 'inc/our-services.html')


from django.template import RequestContext


