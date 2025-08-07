from django.shortcuts import redirect, render,HttpResponse
from .models import UserProfile

# Create your views here.
def demo(request):
    return HttpResponse("this is todo app")

def index(request):
    return render (request,"index.html")

def insert(request):
    if request.GET:
        yourname=request.GET['uname']
        mobile=request.GET['number']
        father=request.GET['fname']
        email=request.GET['email']
        password=request.GET['pass']
        user=UserProfile(yourname=yourname,mobile_number=mobile,father_name=father,email_id=email,password=password)
        user.save()
    return render(request,"insert.html")


def show(request):
    data= UserProfile.objects.all()
    print(data)
    return render (request,'show.html',{'keys': data})


def update(request): 
    id=request.GET["id"]
    data=UserProfile.objects.filter(id=id)
    return render (request,"update.html",{"keys": data})

def delete(request):
    id=request.GET['id']
    # print(id)
    UserProfile.objects.filter(id=id).delete()
    data= UserProfile.objects.all()
    print(data)
    return render (request,'show.html',{'keys': data})
    return HttpResponse("data after deletion")


def completeupdate(request):
    if request.GET:
        id=int(request.GET["id"])
        data=UserProfile.objects.filter(id=id).first()
        yourname=request.GET['uname']
        mobile_number=request.GET['number']
        father_name=request.GET['fname']
        email_id=request.GET['email']
        data.email_id=email_id
        data.save()
        # UserProfile(yourname=yourname,mobile_number=mobile_number,father_name=father_name,email_id=email_id).save()
    return render(request,"complete.html")