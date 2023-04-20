from django.shortcuts import render
from app1.models import *
from app1.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('topic insertion done')


    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WPO=WebpageForm()
    d={'WPO':WPO}
    if request.method=='POST':
        WOD=WebpageForm(request.POST)
        if WOD.is_valid():
            WOD.save()
            return HttpResponse('webpage insertion is done successfuly...')


    return render(request,'insert_webpage.html',d)


def insert_AccessRecord(request):
    ARO=AccessRecord()
    d={'ARO':ARO}
    if request.method=='POST':
        ARD=AccessRecord(request.POST)
        if ARD.is_valid():
            ARD.save()
            return HttpResponse('accessRecord insertion is done successfully....')


    return render(request,'insert_AccessRecord.html',d)
