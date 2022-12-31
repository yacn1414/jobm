from django.shortcuts import render,redirect
from jobs import models
# Create your views here.
def workEnd(request):
    pass
def workNow(request):
    return HttpResponse("ok")
def allJobs(request):
    allJob = models.jobs.objects.all()
    a = ""
    for i in request.user.groups.all():
        a += str(i)
    if request.user.is_authenticated:
        return render(request, 'index2.html',{"jobs":allJob,"staff":a})
        
    else:
        return redirect('/signup')
def visit(request,id):
	pass