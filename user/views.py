from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse,HttpResponseBadRequest,HttpResponseRedirect
from django.template import loader,Context,context
from django.shortcuts import render_to_response,render,HttpResponse

# Create your views here.
import logging
import json
import  simplejson
from .models import User
from django import forms

def test(request):
    t = loader.get_template('test.html')
    c = context.Context({'test':'test page'})
    #return  HttpResponse(t.render(c))#baocuo?????

    return  render_to_response('test.html',{'test':'test __page'})
def reg(request:HttpRequest):

    name = request.POST['name']
    password = request.POST['password']
    email = request.POST['email']
    mgr = User.objects.filter(email__contains=3).all()

    print(mgr)

    if mgr :
        return HttpResponseBadRequest('email exist')
    else:
        user = User()
        user.name =name
        user.password=password
        user.email=email
        user.save()
        return HttpResponse('success')

from .forms import UserForm
#文件上传
def register(request):
    if request.method=='POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data['name'],form.cleaned_data['headimage'].name)
            with open('upload/'+form.cleaned_data['headimage'].name,'wb') as f:
                f.write(form.cleaned_data['headimage'].read())
            return HttpResponseRedirect('/')
            #return HttpResponse('ok')
    else:
        form = UserForm()
        return render_to_response('register.html',{'form':form})

#-----------------------------------------------------------------
#cookie session
from .forms import RegisterForm
def register2(request):
    if request.method=='POST':
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            username = registerform.cleaned_data['username']
            password = registerform.cleaned_data['password']
            email = registerform.cleaned_data['email']
            User.objects.create(name=username,password=password,email=email)
            return HttpResponseRedirect('/user/login2/')
    else:
        registerform = RegisterForm()
        return render_to_response('register2.html',{'regiterform':registerform})

def login2(request):
    if request.method=='POST':
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            username = registerform.cleaned_data['username']
            password = registerform.cleaned_data['password']
            #email = registerform.cleaned_data['email']
            user =  User.objects.filter(name__exact=username,password__exact=password)
            if user:
                #session
                request.session['username']=username
                return HttpResponseRedirect('/user/index2/')
                #cookie
                #response = HttpResponseRedirect('/user/index2/')
                #response.set_cookie('username',username,max_age=3600)
                #return  response
    else:
        registerform = RegisterForm()
        return render_to_response('login2.html',{'registerform':registerform})



def index2(request):
    #cookie
    #username = request.COOKIES.get('username','anyone')
    #session
    username = request.session.get('username','someone')
    return render_to_response('index2.html',{'username':username})

def logout(request):

    #或者一cookie
    """
    response = HttpResponse('logout')
    response.delete_cookie('username')
    return response
    """
    #或者二cookie
    """
    response = HttpResponseRedirect('/user/index2/')
    response.delete_cookie('username')
    return response
    """
    #session
    del request.session['username']
    return HttpResponseRedirect('/user/index2')


#
from .forms import LoginForm

def login3(request):
    if request.method=='GET':
        loginform = LoginForm()
        return render_to_response('login3.html',{'loginform':loginform})
    else:
        obj = LoginForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            return HttpResponse('sucess')
        else:

            return render_to_response('login3.html',{'loginform':obj})


def ajax_login(request):
    ret = {'status': True, 'msg': None}
    if request.method=='GET':
        return render_to_response('login3_ajax.html')
    else:
        obj = LoginForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            ret['msg']=obj.cleaned_data
            print(ret)
            return HttpResponse(json.dumps(ret),content_type='application/json')
        else:
            return render_to_response('login3_ajax.html')
def alogin(request):
    """
     ajax  post
    :param request:
    :return:
    """
    print('*'*20)
    if request.method=='POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name=='pig':
            #return HttpResponse(1)

            return HttpResponse('{"status":"success"}')
        else:
            return HttpResponse('{"status":"fail","msg":"用户名或密码错误"}')
    else:

        name = request.GET.get('name')
        password = request.GET.get('password')
        #print(name,password)
        return HttpResponse('your name :{},your password :{}'.format(name,password))