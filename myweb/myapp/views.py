from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random
def hi(request):
    return HttpResponse('<p>13232252222222222222222222222222222223</p>')
# Create your views here.
def hi2(request,username):
    today = datetime.date.today()
   
    return render(request,'hello3.html',{'username':username,'now':today})
def hi4(request,username):
    now = datetime.date.today()

    return render(request,'hello4.html',locals())
def main(request):
    return HttpResponse('<h1>123213</h1>')
def test_dict(request):
    dict1 = {'key1':123,'key2':456}
    now = datetime.date.today()
    return render(request,'hello4.html',locals())
times=0
def dice(request):
    global times
    times=times+1 
    no=random.randint(1,6)
    local_times=times
    return render(request,'dice.html',locals())
def dice3(request):
    global times
    times=times+1 
    username="7414"
    local_times=times
    dict_no={"no":random.randint(1,6)}
    return render(request,'dice3.html',locals())
def show(request):
    person1={"name":"Amy","phone":"049-1234567","age":20}
    person2={"name":"Jack","phone":"02-4455666","age":25}
    person3={"name":"Nacy","phone":"04-9876543","age":17}
    persons=[person1,person2,person3]
    num1 = dict()
    num2 =dict()
    total =[[0]*10 for i in range(10)]
  
    for i in range(1,10):
        num1[i]=i
        num2[i]=i
 
            
    return render(request,"show.html",locals())

