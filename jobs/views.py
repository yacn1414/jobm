from django.shortcuts import render,redirect
from jobs.models import sabtjob,jobs
from django.contrib.auth.models import User
from django.http import HttpResponse
from main.models import customUser
# Create your views here.
def workEnd(request):
    pass
def workNow(request):
    if request.user.is_authenticated:

        job = sabtjob.objects.filter(id_emploee__id=request.user.id)
        cjob = sabtjob.objects.filter(id_emploee__id=request.user.id).count()
        return render(request,"process.html",{"jobs":job,"count":cjob,"emploee":1})
    else:
        return redirect('/')
def allJobs(request):
    allJob = jobs.objects.all()
    a = ""
    for i in request.user.groups.all():
        a += str(i)
    if request.user.is_authenticated:
        return render(request, 'index2.html',{"jobs":allJob,"staff":a})
        
    else:
        return redirect('/signup')
def visit(request,id,employer):
    id_now_user = request.user.id
    if request.user.is_authenticated:
        jjob = jobs.objects.get(id=id)
        users = User.objects.get(username=employer)
        userss = customUser.objects.get(user__id=request.user.id)
        sabtjob.objects.create(id_emploee=userss,id_employer=users,id_job=jjob)
        if jobs.objects.get(id=id).countem > 0:
            jobs.objects.filter(id=id).update(countem = --1)
        else:
            jobs.objects.filter(id=id).delete()
        return redirect('../')