from django.shortcuts import render,redirect
from .models import namesmodel
from .forms import NamesForm

# Create your views here.
def allifmaalmaindashboard(request):
    context={

    }
    return render(request,'allifmainapp/dashboard/allifmaaldashboard.html',context)
def fortestingonly(request):
    allif="Welcome to Allifmaal Engineering Ltd ... Where career dreams come true!"
    context={
        "allif":allif,

    }
    return render(request,'allifmainapp/dashboard/candelete.html',context)

# Create your views here.
def nameregistpage_testing_only(request):
    names=namesmodel.objects.all()

    form=NamesForm()
    
    if request.method=='POST':
        form=NamesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
           
            return redirect('allifmainapp:nameregistpage_testing_only')
    context={
        "form":form,
        "names":names,
    }
    return render(request,'allifmainapp/dashboard/nameregist.html',context)
    return render(request,'myhomepage.html',context)