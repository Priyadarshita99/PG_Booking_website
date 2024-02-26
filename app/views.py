from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *

def dummy(request):
    return render(request,'dummy.html')

def insert_pg(request):
    EFPO=PgForm()
    d={'EFPO':EFPO}

    if request.method=='POST':
        DFPO=PgForm(request.POST)
        if DFPO.is_valid():
            DFPO.save()
            return HttpResponse('PG Inserted Successfully')
    return render(request,'insert_pg.html',d)

def display_pg(request):
    QLPO=Pgs.objects.all()
    d1={'QLPO':QLPO}
    return render(request,'display_pg.html',d1)