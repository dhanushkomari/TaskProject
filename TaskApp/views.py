from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.models import User,Group
from .forms import SignUpFormSP,SignUpFormClient
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django import template
from django.views.generic.edit import CreateView

register = template.Library()

# Create your views here.


def welcome(request):
    #SP = Group.objects.filter(name="SERVICE_PROVIDERS")
    # sp =Group.objects.all()
    sp = User.objects.filter(groups__name="SERVICE_PROVIDERS")
    

    print(sp)
    return render(request,'TaskApp/adminprofile.html',{'sp':sp})
    





###################################
#########  HOME VIEW   ############
###################################
class Home(TemplateView):
    template_name = 'TaskApp/index.html'

class adminprofile(TemplateView):
    template_name = 'TaskApp/adminprofile.html'


#################################################
#########  SIGN UP FOR SERVICE PROVIDER #########
#################################################
def SignUpSPView(request):
    if request.method == 'POST':
        form = SignUpFormSP(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            signup_user = User.objects.get(username=username)
            sp_group = Group.objects.get(name='SERVICE_PROVIDERS')
            sp_group.user_set.add(signup_user)
    else:
            form = SignUpFormSP()
    return render(request,'accounts/sp_signup.html',{'form':form})

#################################################
#########  SIGN UP FOR CLIENT   #################
#################################################

def SignUpClientView(request):
    if request.method == 'POST':
        form = SignUpFormClient(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            signup_user = User.objects.get(username=username)
            sp_group = Group.objects.get(name='CLIENTS')
            sp_group.user_set.add(signup_user)
    else:
        form = SignUpFormClient()
    return render(request,'accounts/client_signup.html',{'form':form})

###################################################
#########  SIGN IN FOR SERVICE PROVIDER  ##########
###################################################

def loginSPView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user.groups.filter(name='SERVICE_PROVIDERS').exists():
                if user is not None:
                    login(request,user)
                    return redirect('landing')
            else:
                return HttpResponse(" User Does not Exist")
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

###################################################
#########  SIGN IN FOR CLIENTS ####################
###################################################

def loginClientView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user.groups.filter(name='CLIENTS').exists():
                if user is not None:
                    login(request,user)
                    return redirect('AppPost:post-list')
            else:
                return HttpResponse(" User Does not Exist")
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

###########################################      
############     LOGOUT VIEW   ############
###########################################

def SignOutView(request):
    logout(request)
    return redirect('landing')

###########################################
##########   admin custom login ###########
###########################################


def LoginAdminView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password) 
            if user.is_staff:           
                if user is not None:
                    login(request,user)
                    return redirect('TaskApp:home')
                else:
                    return HttpResponse(" User Does not Exist")
            else:
                return HttpResponse("<h2>You are no longer Admin</h2>")
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
