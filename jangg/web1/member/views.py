from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


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
        id=request.POST['id']
        pw=request.POST['pw']
        name=request.POST['name']
        yy=request.POST['yy']
        mm=request.POST['mm']
        dd=request.POST['dd']
        gd=request.POST['gd']
        em=request.POST['em']
        ph=request.POST['ph']
        ar=[id,pw,name,yy,mm,dd,gd,em,ph]

        sql='''
            INSERT INTO ID,PW,NAME,YY,MM,DD,GD,EM,PH,JOINDATE
            VALUES(%s, %s, %s, %s,%s,%s,%s,%s,%s, SYSDATE)
        '''
        cursor.execute(sql, ar)

        return redirect("/member/index")

@csrf_exempt
def login(request):
    if request.method=='GET':
        return render(request, 'member/login.html')
    elif request.method=='POST':
        


        return redirect('/member/index')