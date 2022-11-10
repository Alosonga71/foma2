from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect

# Create your views here.

def persondetails(request):
    quieryset = person.objects.all()
    context   = {
        'quieryset':quieryset
    }
    return render(request, 'index.html', context)

def personview(request, id):
    man  = person.objects.get(id=id)
    context  = {
        'man': man
    }
    return render(request, 'personview.html', context)

def addingPerson(request):
    form = addPerson()

    if request.method == 'POST':
        form = addPerson(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    
    context = {
        'form': form
    }
    return render(request, 'form.html', context)

def thankView(request):
    pass



def laptopdetails(request):
    product = laptop.objects.all()
    context = {
        'product':product
    }
    return render(request, 'index.html', context)