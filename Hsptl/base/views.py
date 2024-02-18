from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .form import *
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password =request.POST['password']
        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        return redirect ('login')
    return render(request,'signup.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            response = redirect('home')  # Redirect to the home page

            response.set_cookie('username', username)  # Set username as a cookie
            return response
            # return redirect ('home')
        else:
            return redirect('signup')
    
    if 'username' in request.COOKIES:
        context={
             'username':request.COOKIES['username']
             }
        return render(request,'home.html',context)

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    # Manually delete a cookie
    response = redirect('home')
    response.delete_cookie('username')  # Delete the username cookie
    return response
    # return redirect ('home')

def home(request):
    return render(request,'home.html')

def departments(request):
    dict={
        'dep':Departments.objects.all()
    }
    return render(request,'department.html',dict)

@login_required
def booking(request):
    if request.method == 'GET':
        context={}
        context['form']=BookingForm()
        return render(request,'booking.html',context)
    elif request.method == 'POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
         context={}
         context['form']=BookingForm()
         return render(request,'booking.html',context)
  

def doctors(request):
    doct={
        'doc':Doctors.objects.all()
    }
    return render(request,'doctor.html',doct)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')



class DocDetailView(DetailView):
   model = Doctors
   template_name = 'docdetail.html'
   context_object_name = 'doc'
   
