from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import *
from app1.models import *


def sCCC(request):
    SIO=Sch()
    if request.method=='POST':
        sss=Sch(request.POST)
        if sss.is_valid():
            sss.save() #We are not collecting the cleaned_date ,... this method automatically do this process (collecting the data, updating that data to tables),.... it is also advantage for model forms,....
            return HttpResponse('Successfully created in SchoolInfo Table')
    dd={'SIO':SIO} 
    return render(request,'h1.html',dd)



def sTTT(request):
    STIO=Std()
    if request.method=='POST':
        sss=Std(request.POST)
        if sss.is_valid():
            sss.save()
            return HttpResponse('Successfully created in StudentInfo Table')
    dd={'STIO':STIO} 
    return render(request,'h2.html',dd)

