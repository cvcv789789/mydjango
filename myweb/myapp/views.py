from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hi(request):
    return HttpResponse('<p>13232252222222222222222222222222222223</p>')
# Create your views here.
def hi2(request,username):
    today = datetime.date.today()
   
    return render(request,'hello3.html',locals())#locals把DEF 裡面的所有變數 打包成字典 
def main(request):
    return HttpResponse('<h1>123213</h1>')