from django.shortcuts import render
from .models import newstable
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
import os
# Create your views here.
def index(request):
    print(os.path.join(settings.BASE_DIR, 'static'))
    return render(request,'index2.html')


def newshandle(request):
    count=newstable.objects.filter(Q(isDelete=False)|Q(isDelete__isnull=True)).filter(Q(area__isnull=True)|Q(important__isnull=True)).count()
    if count==0:
        return  HttpResponse('暂时没有需要处理的消息呢！么么哒')
    news=newstable.objects.filter(Q(isDelete=False)|Q(isDelete__isnull=True)).filter(Q(area__isnull=True)|Q(important__isnull=True)).first()

    return render(request, 'newshandle2.html',{'news': news,'count':count})


def save(request):
   # print(request.POST)
    modify=newstable.objects.get(id=request.POST.get("id"))
    #print(modify.isDelete)
    modify.news=request.POST.get("news")
    modify.area=request.POST.get("area")
    modify.important=request.POST.get("important")
    modify.note=request.POST.get("note")
    if request.POST.get("isDelete") =="1":
        modify.isDelete=True
        #print(modify.isDelete)
    else:modify.isDelete=False
    modify.save()

    return HttpResponseRedirect('/newshandle/')

def newshandletest(request):
    count=newstable.objects.filter(Q(isDelete=False)|Q(isDelete__isnull=True)).filter(Q(area__isnull=True)|Q(important__isnull=True)).count()
    if count==0:
        return  HttpResponse('暂时没有需要处理的消息呢！么么哒')
    news=newstable.objects.filter(Q(isDelete=False)|Q(isDelete__isnull=True)).filter(Q(area__isnull=True)|Q(important__isnull=True)).first()

    return render(request, 'newshandle2.html',{'news': news,'count':count})


def savetest(request):
    print(request.POST)
    # modify=newstable.objects.get(id=request.POST.get("id"))
    # print(modify.isDelete)
    # modify.news=request.POST.get("news")
    # modify.area=request.POST.get("area")
    # modify.important=request.POST.get("important")
    # modify.note=request.POST.get("note")
    # if request.POST.get("isDelete") =="1":
    #     modify.isDelete=True
    #     print(modify.isDelete)
    # else:modify.isDelete=False
    return HttpResponseRedirect('/newshandletest/')


from datetime import datetime,timedelta
import time
def newssearch(request):

    if request.POST.get('important'):
        print(request.POST)
        begins=request.POST.get('begindate')
        ends=request.POST.get('enddate')
        begins+='-13'
        ends+='-13'
        begin=datetime.strptime(begins,"%Y-%m-%d-%H")
        end=datetime.strptime(ends,"%Y-%m-%d-%H")
        # print(type(begin),end)
        # print(request.POST.getlist('important'))
        count = newstable.objects.filter(isDelete=False).filter(datetime_list__range=(begin,end)).filter(important__in=request.POST.getlist('important')).count()
        #print(count)
        # frist = newstable.objects.filter(isDelete=False).filter(datetime_list__range=(begin,end)).order_by('datetime_list').first()
        # print(frist.datetime_list)
        allnews = newstable.objects.filter(isDelete=False).filter(datetime_list__range=(begin,end)).order_by('datetime_list').filter(important__in=request.POST.getlist('important'))
        # if 1 in request.POST.get('area')
        dic={
            '1':'us',
            '2':'cn',
            '3':'eu',
            '4':'oi',
            '5':'ja',
            '6':'lu',
            '7':'au',
            '8':'ot',

        }
        relist={}
        for i in request.POST.getlist('area'):

            relist.update({dic[i]:allnews.filter(area=i)})




        us = allnews.filter(area='1')
        cn = allnews.filter(area='2')
        eu = allnews.filter(area='3')
        oi = allnews.filter(area='4')
        ja = allnews.filter(area='5')
        lu = allnews.filter(area='6')
        au = allnews.filter(area='7')
        ot = allnews.filter(area='8')
    else:return render(request,'search.html')



    return render(request,'search.html',{'us':us,'cn':cn,'eu':eu,'oi':oi,'ja':ja,'lu':lu,'au':au,'ot':ot})



def postnews(request):
    if request.method == "POST":

        id_n=request.POST.get('id')
        news=newstable.objects.get_or_create(id=id_n)

        x=id_n[:14]
        datetime_n=x[:4]+"-"+x[4:6]+"-"+x[6:8]+' '+x[8:10]+':'+x[10:12]+':'+x[12:]

        news[0].datetime_list=datetime_n

        news[0].news = request.POST.get("news")

        news[0].isDelete = False
        news[0].save()

        return HttpResponse('ok')
