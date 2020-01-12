from django.db import models

# Create your models here.
class table(models.Model):
    object = models.Manager()#vs code 오류 제거용

    id     = models.AutoField(primary_key = True)#게시판 글 = 기본키 
    pw   = models.CharField(max_length=200)#비밀번호
    name = models.CharField(max_length=20)
    yy = models.IntegerField()
    mm = models.IntegerField()
    dd = models.IntegerField()
    gd = models.CharField(max_length=20)
    em = models.TextField()
    ph = models.IntegerField()
    regdate = models.DateField(auto_now_add=True)