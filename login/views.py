from django.shortcuts import render, redirect
from . import models

def index(request):


    return render(request, './login/index.html')
    


def login(request):
    if request.session.get('loginFlag',None):
        return redirect('/')


    if request.method == 'POST':
        email = request.POST.get('email',None)     
        pwd = request.POST.get('password',None)
        if email and pwd:
            user = models.User.objects.filter(email=email)
            if user:
                _pwd = user[0].pwd
            else:
                return render(request, './login/login.html')
            if pwd == _pwd:
                request.session['loginFlag'] = True
                request.session['username'] = user[0].name
                return redirect('/')
            else:
                return render(request, './login/login.html')
    return render(request, './login/login.html')

    
def register(request):

    if request.method == 'POST':
        email = request.POST.get('email',None)
        name = request.POST.get('name',None)
        pwd1 = request.POST.get('password1',None)
        pwd2 = request.POST.get('password2',None)

        if pwd1 == pwd2:
           user = models.User.objects.filter(email=email)
           if user:
              print("此帳戶已經被註冊")
              return redirect( '/register/')
           new_user = models.User.objects.create()
           new_user.email = email
           new_user.name = name
           new_user.pwd = pwd1
           new_user.save()
           return redirect( '/login/')
           
        


  
    return render(request, './login/register.html')


def logout(request):
    if request.session.get('loginFlag',None):
        request.session.flush()
        return redirect( '/login/')


    return redirect( '/')



