from django.shortcuts import render,redirect
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from main import models
from jobs.models import jobs,sabtjob
# Create your views here.
def main(request):
    online = 1
    kasbCount = jobs.objects.count()
    allUserCount = models.customUser.objects.count()
    return render(request, 'index.html',{"online":online,"kasbCount":kasbCount,"userCount":allUserCount})
def registeration(request):
    return render(request,'registeration/signup.html',{})
def auth(request):
    
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST['username']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        password = request.POST['password']
        moduser = User.objects.create_user(username=username,email=email,password = password,first_name=fname,last_name=lname)
        upd = models.customUser.objects.create(user=moduser,city=city,state=state,address=address)
        my_group1 = Group.objects.get(name='emploee')
        my_group2 = Group.objects.get(name='employer')
        if request.POST.get('ok') is not None:
            my_group2.user_set.add(moduser)
        else:
            my_group1.user_set.add(moduser)
            
        if moduser is not None:
            if moduser.is_active:
                request.session.set_expiry(86400)
                login(request, moduser)
                return redirect('/account/')
            else:
                messages.ERROR(request,'مشکلی در ثبت نام وجود دارد')
                return redirect('/signup/')
        # return render(request, 'profile.html',{})
    else:
        return redirect('/')

def account(request):
    a = ""
    for i in request.user.groups.all():
        a += str(i)
    return render(request, 'account.html',{"group":a})
def log_in(request):
    return render(request, 'registeration/login.html')
def authlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/account/')
            
        else:
            # bug
            return redirect('/login/')
            
    return redirect('/login')
    
def add(request):

    return render(request,'add.html')
def adda(request):
    if request.method == 'POST':
        idem = models.customUser.objects.get(user__id=request.user.id)
        title = request.POST['title']
        description = request.POST['description']
        countperson = request.POST['countperson']
        image = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save("static/image/jobs/" + image.name, image)
        file_url = fss.url(file)
        jobs.objects.create(idemployer=idem,title=title,description=description,countem=countperson,image=image,status="open")
    return render(request,'add.html')
def procces(request):
    job = sabtjob.objects.filter(id_job__idemployer__user__id=request.user.id)
    a = {}
    for jo in job:
        if jo.vaziat == "open":
            a += jo
    return render(request,"process.html",{"jobs":a})
def ended(request,id):
    data = sabtjob.objects.get(id=id)
    data.vaziat = "close"
    data.save()
    return redirect('/procces')
