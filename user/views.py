from functools import wraps

from django.shortcuts import render,HttpResponse
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout #用户认证
from django.views.decorators.http import require_POST,require_GET
from django.contrib.auth.decorators import login_required

from messages import Messages
import simplejson

@require_POST
def reg(request:HttpRequest):
    print(request.body)
    print(request.POST)
    print(request.GET)
    print("==============")
    try:
        payload=simplejson.loads(request.body)
        print(type(payload),payload) #dict

        #判断用户是否存在
        username=payload["username"]
        count=User.objects.filter(username=username).count()
        if count>0:
            return JsonResponse(Messages.USER_EXISTS)
        #数据存储
        email=payload["email"]
        password=payload["password"]
        usr=User.objects.create_user(username,email,password)
        print(type(usr),usr) #创建成功或登录成功看到User实例

        return HttpResponse({},status=201)
    except Exception as e:
        return JsonResponse(Messages.BAD_REQUEST,status=200)

@require_POST
def log(request:HttpRequest):
    #进入到视图函数中，request中应当有2个动态增加属性，session，user，中间件动态注入
    try:
        payload=simplejson.loads(request.body)
        username = payload["username"] #登录如何处理？
        password = payload["password"]
        user=authenticate(username=username,password=password) #用户名和密码匹配，和数据库记录一一对应则匹配成功，真实用户is_authenticate永远是True
        print(type(user),user) #返回User名匹配成功，None匹配失败
        print("=================")
        print(type(request.user),request.user)  #匿名用户,但是is_authenticate永远是Flase
        print(type(request.session),request.session)
        if user :
            # cookie和session，首先必须对认证成功的用户发放一个身份id，response中增加set—cookie，至少应该有sid。sid必须保存在服务器端
            login(request,user) #与当前用户创建session，将真实用户捆绑到request上，各类后台jsp，php都习惯用request.session取session值
            from django.contrib.sessions.backends.db import SessionStore
            session:SessionStore=request.session
            session.set_expiry(1200)  #设置过期时间
            session["userinfo"]={
                "id":request.user.id,
                "username":request.user.username
            } #定义用户session信息保存在内存中
            response=HttpResponse(status=204)
            # response.set_cookie({"session-id":""})
            return response
        return JsonResponse(Messages.INVALID_USERNAME_OR_PASSWORD,status=200)
    except Exception as e:
        return JsonResponse(Messages.BAD_REQUEST,status=200)

def login_required(exclude_methods=None):     #自定义认证装饰器
    def _login_required(viewfunc):
        @wraps(viewfunc)
        def wrapper(request,*args,**kwargs):
            nonlocal exclude_methods
            method=request.method.lower()
            if exclude_methods is None:
                exclude_methods=[]
            exclude_methods=[x.lower() for x in exclude_methods]
            if method in exclude_methods: #不认证
                return viewfunc(request,*args,**kwargs)
            else:
                if request.user.is_authenticated:
                    print("认证通过！")
                    return viewfunc(request,*args,**kwargs)
                else:
                    print("认证未通过！")
                    return HttpResponse(status=401)
        return wrapper
    if callable(exclude_methods):
        #bug
        fn=exclude_methods
        exclude_methods=None
        return _login_required(fn)
    return _login_required

@login_required #有默认跳转路径,会拦截
# @login_required(login_url='/users/login')
def log_o(request:HttpRequest):
    print("+"*30)
    print(request.user)
    print(request.user.__dict__)
    print(*request.session.items(),sep="\n")
    logout(request) #request.session request.user 清空当前用户登录状态，包括其相关session和数据库记录，彻底作废
    print(request.session.items())
    return HttpResponse("登出成功！",status=200)

