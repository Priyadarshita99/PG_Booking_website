from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from app.forms import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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

def view_details(request):
    return render(request,'view_details.html')

def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}

    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            mufdo=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            mufdo.set_password(pw)
            mufdo.save()

            mpfdo=pfd.save(commit=False)
            mpfdo.username=mufdo
            mpfdo.save()

            send_mail('registration',
            'form register successfully',
            'cprasanth652@gmail.com',
            [mufdo.email],
            fail_silently=False,
            )
            return HttpResponse('data submitted')
        else:
            return HttpResponse('invalid data')
    return render(request,'registration.html',context=d)

def login_page(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('dummy'))
        else:
            return HttpResponse('Incorrect Username or Password.Please try again.')
    return render(request,'login_page.html')

@login_required
def display_profile(request):
    un=request.session.get('username')
    uo=User.objects.get(username=un)
    po=Profile.objects.get(username=uo)
    d={'uo':uo,'po':po}
    return render(request,'display_profile.html',d)

def booking(request):
    EBFO=BookingForm()
    d={'EBFO':EBFO}
    return render(request,'booking.html',d)

def view_details(request):
    return render(request,'view_details.html')

def payment(request):
    return render(request,'payment.html')