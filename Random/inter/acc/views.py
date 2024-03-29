from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import  CreateUserForm
# from .filters import OrderFilter


# Create your views here.

def front(request):
    return render(request , 'acc/front.html')
    # return HttpResponse('Front Page')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('front')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user )
                return redirect('login')
        context = {'form':form}
        return render(request, 'acc/register.html',context)
# 
def loginPage(request):
    # context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request , user)
            return redirect('cust')

        else:
            messages.info(request , 'Username OR Password is incorrect')
            return render(request, 'acc/login.html')


    return render(request, 'acc/login.html')



def new(request):
    # if request.user.is_authenticated:
        return redirect('cust')
    # else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user )
                return redirect('login')
        context = {'form':form}
        return render(request, 'acc/new.html',context)

# def register(request):
    # return HttpResponse('Customer Page')

# def customerr(request):
    # customers = customer.objects.all()
    # company = customer_comp.objects.all()
    # jobtype = Job_type.objects.all()
    # jobprofile = job_profile.objects.all()
    # data = {'customers' : customers , 'comp' : company, 'jobT' : jobtype , 'jobP': jobprofile}
    # return render(request, "acc/customer.html", data)

def interviewees(request):
    # cust = main_customer.objects.get(id = pk_test)
    customers = interviewee.objects.all()
    context = {'customers':customers}
    return render (request, 'acc/customer.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url = 'login')

def jobtype(request):
    jobtypes = Job_type.objects.all()
    data = {'jobtype':jobtypes}
    render(request, 'acc/customer.html',data)

