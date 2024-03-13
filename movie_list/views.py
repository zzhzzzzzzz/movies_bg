import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['axes.unicode_minus']=False

import math

import simplejson
from django.db.transaction import atomic
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.views.decorators.http import require_GET

from .models import WeekMovies,HotMovies,BoxOffice,AllMovies,TopMovies
from messages import Messages
from user.views import login_required

def vaildate(d:dict,name:str,default,type_func,validate_func=lambda x,y:x):
    try: # 从什么里面获取一个指定名称对应的值，如果没拿到给缺省值，将值按给定的转换函数转换，在判断范围，超范围或转换失败给缺省值
        value=type_func(d.get(name,default))
        value=value if value > 0 else default
    except:
        value=default
    return value

class MovieView1(View):
    def get(self,request): #方法名一定是小写
        try:
            page=vaildate(request.GET, 'page', 1 , int , lambda x, y: x if x > 0 and x < 51 else y)
            size=vaildate(request.GET, 'size', 5, int , lambda x, y: x if x > 0 and x < 101 else y)

            start=size*(page-1)
            mgr=WeekMovies.objects
            total=mgr.count()
            movies=WeekMovies.objects.order_by('pk')[start:start+size] #全表

            return  JsonResponse({"movies":[
                {"id":movie.id,"title":movie.title,'rate':movie.rate}
                for movie in movies
            ],
                "pagination":{
                    'page':page,
                    'size':size,
                    'total':total,
                    'pages':math.ceil(total/size),
                }
            })
        except Exception as e:
            return JsonResponse(Messages.BAD_REQUEST)


@require_GET
def getweekmovie(request,id): #详情页
    try:
        movie = WeekMovies.objects.get(pk=id)
        return JsonResponse({'movie': {
            'id': movie.pk,
            'title': movie.title,
            "releasedate": movie.releasedate,  # utc字符串
            "director": movie.director,
            "rate": movie.rate,
            "kind": movie.kind,
            "country": movie.country,
            "language": movie.language,
            "time": movie.time,
            "actor": movie.actor
        }})
    except Exception as e:
        return JsonResponse(Messages.NOT_FOUND)

class MovieView2(View):
    def get(self,request): #方法名一定是小写
        try:
            page=vaildate(request.GET, 'page', 1 , int , lambda x, y: x if x > 0 and x < 51 else y)
            size=vaildate(request.GET, 'size', 5, int , lambda x, y: x if x > 0 and x < 101 else y)

            start=size*(page-1)
            mgr=BoxOffice.objects
            total=mgr.count()
            movies=BoxOffice.objects.order_by('pk')[start:start+size] #全表

            return  JsonResponse({"movies":[
                {"id":movie.id,"title":movie.title,'rate':movie.rate}
                for movie in movies
            ],
                "pagination":{
                    'page':page,
                    'size':size,
                    'total':total,
                    'pages':math.ceil(total/size),
                }
            })
        except Exception as e:
            return JsonResponse(Messages.BAD_REQUEST)

def getboxoffice(request,id): #详情页
    try:
        movie=BoxOffice.objects.get(pk=id)
        return JsonResponse({'movie': {
            'id':movie.pk,
            'title':movie.title,
            "releasedate":movie.releasedate,  #utc字符串
            "director":movie.director,
            "rate":movie.rate,
            "kind":movie.kind,
            "country":movie.country,
            "language":movie.language,
            "time":movie.time,
            "actor":movie.actor
        }})
    except Exception as e:
        return JsonResponse(Messages.NOT_FOUND)

class MovieView3(View):
    def get(self, request):
        try:
            page = vaildate(request.GET, 'page', 1, int, lambda x, y: x if x > 0 and x < 51 else y)
            size = vaildate(request.GET, 'size', 5, int, lambda x, y: x if x > 0 and x < 101 else y)

            start = size * (page - 1)
            mgr = HotMovies.objects
            total = mgr.count()
            movies = HotMovies.objects.order_by('pk')[start:start + size]  # 全表

            return JsonResponse({"movies": [
                {"id": movie.id, "title": movie.title,'rate':movie.rate}
                for movie in movies
            ],
                "pagination": {
                    'page': page,
                    'size': size,
                    'total': total,
                    'pages': math.ceil(total / size),
                }
            })
        except Exception as e:
            return JsonResponse(Messages.BAD_REQUEST)

def gethotmovie(request,id): #详情页
    try:
        movie = HotMovies.objects.get(pk=id)
        return JsonResponse({'movie': {
            'id': movie.pk,
            'title': movie.title,
            "releasedate": movie.releasedate,  # utc字符串
            "director": movie.director,
            "rate": movie.rate,
            "kind": movie.kind,
            "country": movie.country,
            "language": movie.language,
            "time": movie.time,
            "actor": movie.actor
        }})
    except Exception as e:
        return JsonResponse(Messages.NOT_FOUND)

class MovieView5(View):
    def get(self, request):  # 方法名一定是小写
        try:
            page = vaildate(request.GET, 'page', 1, int, lambda x, y: x if x > 0 and x < 51 else y)
            size = vaildate(request.GET, 'size', 5, int, lambda x, y: x if x > 0 and x < 101 else y)

            start = size * (page - 1)
            mgr = TopMovies.objects
            total = mgr.count()
            print(total)
            movies = TopMovies.objects.order_by('pk')[start:start + size]  # 全表

            return JsonResponse({"movies": [
                {"id": movie.id, "title": movie.C_title,'rate':movie.rate}
                for movie in movies
            ],
                "pagination": {
                    'page': page,
                    'size': size,
                    'total': total,
                    'pages': math.ceil(total / size),
                }
            })
        except Exception as e:
            return JsonResponse(Messages.BAD_REQUEST)

def gettopmovie(request,id): #详情页
    try:
        movie = TopMovies.objects.get(pk=id)
        return JsonResponse({'movie': {
            'id': movie.pk,
            'C_title': movie.C_title,
            'E_title': movie.E_title,
            "url": movie.url,
            "director": movie.director,
            "actor": movie.actor,
            "releasedate": movie.releasedate,
            "country": movie.country,
            "kind": movie.kind,
            "rate": movie.rate,
            'people':movie.people,
        }})
    except Exception as e:
        return JsonResponse(Messages.NOT_FOUND)

class MovieView4(View):
    def get(self, request,info):  # 方法名一定是小写
        try:
            page = vaildate(request.GET, 'page', 1, int, lambda x, y: x if x > 0 and x < 51 else y)
            size = vaildate(request.GET, 'size', 5, int, lambda x, y: x if x > 0 and x < 101 else y)

            start = size * (page - 1)
            mgr = AllMovies.objects.filter(title__icontains=info)
            total = mgr.count()
            movies = mgr[start:start + size]

            return JsonResponse({"movies": [
                {"id": movie.id, "title": movie.title,'rate':movie.rate}
                for movie in movies
            ],
                "pagination": {
                    'page': page,
                    'size': size,
                    'total': total,
                    'pages': math.ceil(total / size),
                }
            })
        except Exception as e:
            return JsonResponse(Messages.BAD_REQUEST)

def searchmovie(request,id): #详情页
    try:
        movie = AllMovies.objects.get(pk=id)
        return JsonResponse({'movie': {
            'id': movie.pk,
            'title': movie.title,
            "releasedate": movie.releasedate,  # utc字符串
            "director": movie.director,
            "rate": movie.rate,
            "kind": movie.kind,
            "country": movie.country,
            "language": movie.language,
            "time": movie.time,
            "actor": movie.actor
        }})
    except Exception as e:
        return JsonResponse(Messages.NOT_FOUND)

def pie_data(request):
    try:
        movie = AllMovies.objects.values()
        movie=pd.DataFrame(movie)
        data = movie['country']
        ls = []
        c_ls = []
        c_dic = {}
        for i in data:
            if '/' in i:
                for j in i.split('/'):
                    c_ls.append(j.strip())
            if '/' not in i:
                for j in i.split():
                    c_ls.append(j.strip())
        for x in c_ls:
            c_dic[x] = c_dic.get(x, 0) + 1

        for i in c_dic.items():
            d = {}
            d['value'] = i[1]
            d['name'] = i[0]
            ls.append(d)
        return JsonResponse({'data':ls})
    except Exception as e:
        return JsonResponse(Messages.NOT_FOUND)