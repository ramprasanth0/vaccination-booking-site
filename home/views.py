from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login
# Create your views here.

def home_page(request):                     #
    return render(request,'homepage.html')

def user_page(request):
    return render(request,'user_page.html')

def admin_page(request):
    return render(request,'admin_page.html')

def sign_up(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        # contact_no=request.POST['contact_no']

        if password1!=password2:
            #return redirect('signup_error')
            messages.info(request,'Password does not match')
            return redirect('sign_up')
        elif User.objects.filter(email=email).exists():  
            #return redirect('signup_error')
            messages.info(request,'Email already taken')
            return redirect('sign_up')
        elif User.objects.filter(username=username).exists():
            # return redirect('signup_error')
            messages.info(request,'Username already taken')
            return redirect('sign_up')
        else:
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
            user.save()
            return redirect('login_page')
    
    else:
        return render(request,'sign_up.html')

def user_login_page(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']

        # if User.objects.filter(username=username) and User.objects.filter(password=password):
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/user/')
        else:
            messages.info(request,'Username,Password does not match')
            return redirect('user_login_page')

    else:
        return render(request,'user_login_page.html')

# def signup_error(request):
#     return render(request,'signup_error.html')


def admin_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        # try:                                                                      #method 1
        #     user=User.objects.get(username=username)
        # except User.DoesNotExist:
        #     messages.info(request,'Username,Password does not match')
        #     return redirect('admin_login')
        # else:
        #     if user.is_superuser:
        #         auth_user=authenticate(request,username=username,password=password)
        #         if auth_user is not None:
        #             login(request,auth_user)
        #             return redirect('/admin_access/')
        #         else:
        #             return redirect('admin_login')
        #     else:
        #         return redirect('admin_login')

        admin=auth.authenticate(username=username,password=password)                 #method 2
        auth_admin=User.objects.get(username=username)                               #error not rectified for wrong username
        if admin is not None:
            if auth_admin.is_superuser:
                auth.login(request,admin)
                return redirect('/admin_access/')
        else:
            messages.info(request,'Username,Password does not match')
            return redirect('admin_login')

    else:
        return render(request,'admin_login.html')
