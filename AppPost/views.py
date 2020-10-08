from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from . forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import User
# Create your views here.


################################################
############  POST FORM View   #################
################################################
def PostFormView(request):
    if request.user.groups.filter(name='SERVICE_PROVIDERS').exists():
        current_user = request.user
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                print('form is saved')
                title = request.POST['title']
                description = request.POST['description']
                #slug = request.POST['slug']
                post_info = Post(user=current_user,title=title,description=description)
                post_info.save()
            return redirect('AppPost:post-complete')
        else:       
            form = PostForm    
        return render(request,'AppPost/post_form.html',{'form':form})
    
    else:
        return redirect('landing')

################################################
############  POST LIST VIEW   #################
################################################

def PostList(request):
    #print('request.user')
    if request.user.groups.filter(name='CLIENTS').exists():
        post= Post.objects.all()
        return render(request,'AppPost/post_list.html',{'post':post})
    else:
        return redirect('landing')

def PostComplete(request):    
    if request.user.groups.filter(name='SERVICE_PROVIDERS').exists():
        return render(request,'AppPost/post_complete.html')
    
    else:
        return HttpResponse("Access Denied")

###############################################
############   CONTACT ME VIEW   ##############
###############################################

def  ContactView(request):
    post = Post.objects.all()
    if request.user.groups.filter(name='CLIENTS').exists(): 
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['from_email']
                message = form.cleaned_data['message']
                to_mail = 'sekhar@gmail.com'
                try:
                    send_mail(subject,message,from_email,(to_mail,))
                except BadHeaderError:
                    return HttpResponse('Invalid format of header')
                return redirect('AppPost:success')
        else:
            form = ContactForm()
        return render(request,'AppPost/contact.html',context={'form':form, 'post':post})
    else:
        return HttpResponse("Access Denied")
def SuccessView(request):
    return HttpResponse("Mail has been sent")

##### end of views ##########




