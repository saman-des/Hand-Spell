from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Item
from subprocess import run, PIPE
import sys, io


def index(request):
    # return render(request, 'index.html')
    sign_list = Item.objects.all()
    return render(request, 'index.html', {'sign_list':sign_list})


def addsign(request):
    if request.method == "POST":
        prod = Item()
        prod.name = request.POST.get('name')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, "Sign Added Successfully")
        return redirect('/')

    return render(request, 'addsign.html')

def searchBar(request):
    if request.method == "GET":
        query = request.GET.get('query')
        
        if query:
            items = Item.objects.filter(name__icontains = query)
            return render(request, 'search.html', {'items':items} )
        else:
            print('No info to show')
            return request(request, 'search.html', {})


def runModel(request):
    out = run([sys.executable, 'homesite\model\Sign prediction.py'],
              shell=False, stdout=PIPE)
    print(out.stdout)
    # return HttpResponseRedirect("external")
    return render(request, 'index.html')

# def all_signs(request):
#     sign_list = Item.objects.all()
#     return render(request, 'index.html', {'sign_list':sign_list})