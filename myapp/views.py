from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login ,logout
from django.contrib import messages

from .models import S_Data,T_Data,Batch

# Create your views here.

def index(request):
    # if 'uid' in request.session:
    #     fname = request.session['uid']
    #     return render(request,'index.html',{'fname':fname})
    return render(request, 'index.html')

def form1(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        cpass = request.POST['cpass']
        fname = request.POST['fname']
        phone = request.POST['phone']
        gender = request.POST['gender']
        dob = request.POST['dob']
        student = request.POST['type']

        if password == cpass:
            if User.objects.filter(email = email).exists():
                messages.error(request, 'Email already used')
                return redirect('form1')
            elif User.objects.filter(username = fname).exists():
                messages.info(request, 'Username already used')
                return redirect('form1')
            else:
                user = User.objects.create_user(username = fname,email = email,password = password)
                user.save()
                i = S_Data(u_type=student,e_mail=email,f_name=fname,phone=phone,dob=dob,gender=gender)
                i.save()
                messages.success(request, 'Account created successfully...')
                messages.success(request, 'Visit home page to Login')
                return redirect('form1')
        else:
            messages.warning(request, 'Password not confirmed')
            return redirect('form1')
    else:
        return render(request,'form1.html')

def form2(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        cpass = request.POST['cpass']
        fname = request.POST['fname']
        tutor = request.POST['type']
        phone = request.POST['phone']
        dob = request.POST['dob']
        locality = request.POST['locality']
        overview = request.POST['about']
        qualification = request.POST['qualification']
        expertise = request.POST['expertise']
        lang = request.POST['lang']
        rate = request.POST['rate']
        mode = request.POST['mode']

        if password == cpass:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already used')
                return redirect('form2')
            elif User.objects.filter(username = fname).exists():
                messages.info(request, 'Username already used')
                return redirect('form2')
            else:
                user = User.objects.create_user(username = fname,email = email,password = password)
                user.save()
                j = T_Data(u_type=tutor,e_mail=email,f_name=fname,phone=phone,dob=dob,locality=locality,overview=overview,qualification=qualification,expertise=expertise,languages=lang,rate=rate,mode=mode)
                j.save()
                messages.info(request, 'Account created successfully...')
                messages.info(request, 'Visit home page to Login')
                return redirect('form2')
        else:
            messages.info(request, 'Password not confirmed')
            return redirect('form2')
    else:
        return render(request,'form2.html')

def loginUser(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        password = request.POST['password']
        user = authenticate(username=fname,password=password)
        if user is not None:
            login(request, user)
            request.session['uid'] = fname
            allS = S_Data.objects.all()
            allT = T_Data.objects.all()
            try:
                st = S_Data.objects.get(f_name=fname).u_type
                return render(request,'index.html',{'fname':fname,'st':st,'allT':allT})
            except:
                t = T_Data.objects.get(f_name=fname).u_type
                a = Batch.objects.filter(tutor=fname)
                stu = []
                for i in a:
                    b = S_Data.objects.get(f_name=i.student)
                    stu.append(b)
                return render(request,'index.html',{'fname':fname,'t':t,'allS':allS,'stu':stu})
            # else:
            #     if st=='Student':
            #     elif t=='Tutor':
            #     else:
            #         return render(request,'form2.html')
        else:
            messages.info(request, 'Invalid ')
            return render(request,'index.html')
    else:
        return render(request,'index.html')

def logoutUser(request):
        logout(request)
        return render(request,'index.html')

def all(request,id):
    allS = S_Data.objects.all()
    allT = T_Data.objects.all()
    try:
        st = S_Data.objects.get(f_name=id).u_type
        return render(request,'explore.html',{'fname':id,'allT':allT,'st':st})
    except:
        t = S_Data.objects.get(f_name=id).u_type
        return render(request,'explore.html',{'fname':id,'allS':allS,'t':t})

def explore(request,id):
            allS = S_Data.objects.all()
            allT = T_Data.objects.all()
            try:
                st = S_Data.objects.get(f_name=id).u_type
                x = Batch.objects.filter(student=id)
                tu = []
                for i in x:
                    y = T_Data.objects.get(f_name=i.tutor)
                    tu.append(y)
                return render(request,'explore.html',{'fname':id,'st':st,'tu':tu})
            except:
                t = T_Data.objects.get(f_name=id).u_type
                a = Batch.objects.filter(tutor=id)
                stu = []
                for i in a:
                    b = S_Data.objects.get(f_name=i.student)
                    stu.append(b)
                return render(request,'explore.html',{'fname':id,'t':t,'allS':allS,'stu':stu})

def sub(request,id):
    fname = request.session['uid']
    tut = T_Data.objects.get(f_name=id)
    try:
        t = T_Data.objects.get(f_name=fname).u_type
        return render(request,'profile.html',{'fname':fname,'tut':tut,'t':t})
    except:
        st = S_Data.objects.get(f_name=fname).u_type
        return render(request,'profile.html',{'fname':fname,'tut':tut,'st':st})

def profile(request,id):
    fname = request.session['uid']
    try:
        st = S_Data.objects.get(f_name=fname).u_type
        data = T_Data.objects.get(f_name=id)
        return render(request,'profile.html',{'fname':fname,'data':data,'st':st})
    except:
        t = T_Data.objects.get(f_name=fname).u_type
        std = S_Data.objects.get(f_name=id)
        return render(request,'profile.html',{'fname':fname,'std':std,'t':t})

def hire(request,id):
    fname = request.session['uid']
    data = T_Data.objects.get(f_name=id)
    val = 1
    i = Batch(student=fname,tutor=data.f_name)
    i.save()
    try:
        t = T_Data.objects.get(f_name=fname).u_type
        return render(request,'profile.html',{'data':data,'fname':fname,'val':val,'t':t})
    except:
        st = S_Data.objects.get(f_name=fname).u_type
        return render(request,'profile.html',{'data':data,'fname':fname,'val':val,'st':st})
