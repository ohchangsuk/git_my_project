from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as auth1
from django.contrib.auth import login as login1
from django.contrib.auth import logout as logout1

# Create your views here.


cursor= connection.cursor()

@csrf_exempt
def index(request):
    return render(request, 'member/index.html')

    
@csrf_exempt
def join(request):
    if request.method =='GET':
        return render(request, "member/join.html")
    elif request.method == 'POST':
        na=request.POST['na']
        ida=request.POST['id']
        pw=request.POST['pw']
        em=request.POST['em']        
        obj=User.objects.create_user(
            username=ida,
            password=pw,
            first_name=na,
            email=em
            )
        obj.save()
        
        return redirect("/member/index")

@csrf_exempt
def login(request):
    if request.method=='GET':
        return render(request, 'member/login.html')
    elif request.method=='POST':
         ida = request.POST['ida']
         pw = request.POST['pw']
         obj=auth1(request, username=ida, password = pw)
         print(obj,type(obj))
         if obj is not None:
             login1(request, obj)
                login1()
             request.session['userid']=obj[0]
             request.session['password']=obj[1]
             return redirect('/member/index')

         

         return redirect('/member/login')

def edit(request):
    if request.method=='GET':
        return render(request, 'member/edit.html')        
    elif request.method=='POST':
        return redirect('/member/index')