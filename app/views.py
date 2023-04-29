from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def insert_topic(request):
    d={'TFO':Topicform()}

    if request.method=='POST':
        TD=Topicform(request.POST)
        if TD.is_valid():
            TD.save()
            return HttpResponse('data submited successfully')
        else:
            return HttpResponse('data  is not valid')


    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    d={'WPO':Webpageform()}
    if request.method=='POST':
        WD=Webpageform(request.POST)
        if WD.is_valid():
            WD.save()
            return HttpResponse('data inserted successfully') 
        else:
            return HttpResponse('data is not valid')   
    
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    d={'ARO':Accessrecordform()}

    if request.method=='POST':
        AD=Accessrecordform(request.POST)
        if AD.is_valid():
            AD.save()
            return HttpResponse('Data submited Successfully')
        else:
            return HttpResponse('Invalid data')


    return render(request,'insert_accessrecord.html',d)