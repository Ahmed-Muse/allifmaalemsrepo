from django.shortcuts import render

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
