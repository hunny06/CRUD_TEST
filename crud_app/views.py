from django.shortcuts import render
from .models import UserModel
import hashlib
from django.contrib.auth.hashers import make_password


# Create your views here.
def createUser(request):
        if request.method == "GET":
            users = UserModel.objects.all()
            return render( request,"createUser.html" ,{"user":users})
        if request.method == "POST":
            print(request.POST)
            name = request.POST.get('name')
            password = make_password(request.POST.get('password'))
            profile = request.FILES.get('profile')
            user = UserModel.objects.create(name = name,password = password, profile = profile)
            users = UserModel.objects.all()
            return render( request,"createUser.html" ,{"user":users})
    
def updateUser(request,id):
    if request.method == "GET":
        try:
            user = UserModel.objects.get(id = id)
        except:
            raise Exception("User Not Exsist")
        print(user)
        return render( request,"get_user.html" ,{"user":user})
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        password = make_password(request.POST.get('password'))
        profile = request.POST.get('profile')
        user = UserModel.objects.update(name = name,password = password, profile = profile)
        users = UserModel.objects.all()
        return render( request,"createUser.html" ,{"user":users})

def deleteUser(request,id):
    try:
        user = UserModel.objects.get(id = id)
        user.delete()
    except:
        raise Exception("User Not Exsist")
    users = UserModel.objects.all()
    return render( request,"createUser.html" ,{"user":users})

def getUser(request,id):
        if request.method == "GET":
            try:
                user = UserModel.objects.get(id = id)
            except:
                raise Exception("User Not Exsist")
            print(user)
            return render( request,"get_user.html" ,{"user":user})
        