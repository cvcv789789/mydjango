from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hi(request):
    return HttpResponse('<p>13232252222222222222222222222222222223</p>')
# Create your views here.
def hi2(request,username):
    today = datetime.date.today()
   
    return render(request,'hello3.html',{'username':username,'now':today})
def main(request):
    return HttpResponse('<h1>123213</h1>')