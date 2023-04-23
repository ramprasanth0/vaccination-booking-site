from django.shortcuts import render,redirect
from django.contrib import messages
from User.models import vaccination_centre

# Create your views here.

def admin_access(request):
    if request.method=='Post':
        add_centre=request.POST['add_centre']
        remove_centre=request.POST['remove_centre']
        if add_centre is not None:
            if vaccination_centre.objects.filter(name='add_centre').exists():
                centre=vaccination_centre.objects.create(name='add_centre')
                centre.save
                messages.info(request,'Centre success added')
                return redirect('admin_access')
            else:
                messages.info(request,'Centre already exists')
                return redirect('admin_access')
        elif remove_centre is not None:
            if vaccination_centre.objects.filter(name='remove_centre').exists() == False:
                centre=vaccination_centre.objects.create(name='remove_centre')
                centre.save
                messages.info(request,'Centre success removed')
                return redirect('admin_access')
            else:
                messages.info(request,'Centre already removed')
                return redirect('admin_access')
        else:
            messages.info(request,'Invalid Input')
            return redirect('admin_access')
    else:
        return render(request,'admin_access.html')
