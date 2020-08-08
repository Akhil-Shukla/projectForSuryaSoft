# -*- coding: utf-8 -*-


from django.shortcuts import render
from .models import User,Expense

from django.http import HttpResponse,HttpResponseRedirect

def index(request):

    if request.method=="POST":
        usr=User(name=request.POST.get("customerName"))
        usr.save()
        print(request.body)
        print(request)
        print(request.COOKIES)

        print(request.session)


    obj = User.objects.filter(valid=True)

    return render(request,'index.html',{'obj':obj})

def edit(request):
    return render(request,"edit.html")


def remove(request):
    id = request.GET.get('id', -1)

    User.objects.filter(id=id).update(valid=False)

    return HttpResponseRedirect("/app/index/")

def displayExpence(request):


    print (request.GET.get('id'))
    user=User.objects.get(id=request.GET.get('id',-1))
    print (user.name)
    if request.method=="POST":
        exp=Expense(client_id=user,title=request.POST.get("title"),
                    amount=request.POST.get("amount"),
                    description=request.POST.get("description"))
        exp.save()


    exp=Expense.objects.filter(client_id=user)
    return render(request, 'edit.html', {'user':user,'exp':exp})








