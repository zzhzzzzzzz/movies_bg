import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['axes.unicode_minus']=False
import pandas as pd

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
        other={}
        d1 = {}
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
            if i[1] >= 5:
                d['value'] = i[1]
                d['name'] = i[0]
                ls.append(d)
            else:
                other['其它地区(发布电影数<5的地区集合)'] = other.get('其它地区(发布电影数<5的地区集合)', 0) + i[1]
        for j in other.items():
            d1['value'] = j[1]
            d1['name'] = j[0]
            ls.append(d1)
        return JsonResponse({'data':ls})
    except Exception as e:
        return JsonResponse(Messages.NOT_FOUND)

def bar_data(request):
    try:
        movie = AllMovies.objects.values()
        movie=pd.DataFrame(movie)
        data = movie['kind']
        ls = []
        dic = {}
        for i in data:
            if '/' in i:
                for j in i.split('/'):
                    ls.append(j.strip())
            if '/' not in i:
                for j in i.split():
                    ls.append(j.strip())
        for x in ls:
            dic[x] = dic.get(x, 0) + 1
        return JsonResponse(dic)
    except Exception as e:
        return JsonResponse(Messages.NOT_FOUND)

def hist_data(request):
    try:
        movie = AllMovies.objects.values()
        movie=pd.DataFrame(movie)
        data = movie['time'].dropna()
        ls = []
        t_ls = []
        for i in data:
            ls.append(i)
        for i in ls:
            if '分钟' in i:
                t_ls.append(i[:-2])
        return JsonResponse({'time':t_ls})
    except Exception as e:
        return JsonResponse(Messages.NOT_FOUND)

def line_data(request):
    try:
        movie = AllMovies.objects.values()
        movie=pd.DataFrame(movie)
        data = movie['releasedate'].dropna()
        ls = []
        dic = {}
        for i in data:
            i = i[:4]
            ls.append(i)
        for x in ls:
            dic[x] = dic.get(x, 0) + 1
        return JsonResponse(dic)
    except Exception as e:
        return JsonResponse(Messages.NOT_FOUND)

class MovieView6(View):
    def get(self, request):  # 方法名一定是小写
        try:
            page = vaildate(request.GET, 'page', 1, int, lambda x, y: x if x > 0 and x < 51 else y)
            size = vaildate(request.GET, 'size', 5, int, lambda x, y: x if x > 0 and x < 101 else y)

            start = size * (page - 1)
            mgr = AllMovies.objects.filter(releasedate__istartswith='20')
            total = mgr.count()
            movies = mgr[start:start + size]

            return JsonResponse({"movies": [
                {"id": movie.id, "title": movie.title,'rate':movie.rate,'release_date':movie.releasedate}
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

class MovieView7(View):
    def get(self, request):  # 方法名一定是小写
        try:
            page = vaildate(request.GET, 'page', 1, int, lambda x, y: x if x > 0 and x < 51 else y)
            size = vaildate(request.GET, 'size', 5, int, lambda x, y: x if x > 0 and x < 101 else y)

            start = size * (page - 1)
            mgr = AllMovies.objects.filter(releasedate__istartswith='199')
            total = mgr.count()
            movies = mgr[start:start + size]

            return JsonResponse({"movies": [
                {"id": movie.id, "title": movie.title,'rate':movie.rate,'release_date':movie.releasedate}
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

class MovieView8(View):
    def get(self, request):  # 方法名一定是小写
        try:
            page = vaildate(request.GET, 'page', 1, int, lambda x, y: x if x > 0 and x < 51 else y)
            size = vaildate(request.GET, 'size', 5, int, lambda x, y: x if x > 0 and x < 101 else y)

            start = size * (page - 1)
            mgr = AllMovies.objects.filter(releasedate__istartswith='198')
            total = mgr.count()
            movies = mgr[start:start + size]

            return JsonResponse({"movies": [
                {"id": movie.id, "title": movie.title,'rate':movie.rate,'release_date':movie.releasedate}
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

class MovieView9(View):
    def get(self, request):  # 方法名一定是小写
        try:
            page = vaildate(request.GET, 'page', 1, int, lambda x, y: x if x > 0 and x < 51 else y)
            size = vaildate(request.GET, 'size', 5, int, lambda x, y: x if x > 0 and x < 101 else y)

            start = size * (page - 1)
            mgr = AllMovies.objects
            total = mgr.count()
            movies = AllMovies.objects.order_by('pk')[start:start + size]  # 全表

            return JsonResponse({"movies": [
                {"id": movie.id, "title": movie.title,'rate':movie.rate,
                 'release_date':movie.releasedate,'kind':movie.kind}
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

class MovieView10(View):
    def get(self, request):  # 方法名一定是小写
        try:
            page = vaildate(request.GET, 'page', 1, int, lambda x, y: x if x > 0 and x < 51 else y)
            size = vaildate(request.GET, 'size', 5, int, lambda x, y: x if x > 0 and x < 101 else y)

            start = size * (page - 1)
            mgr = AllMovies.objects.filter(kind__icontains='剧情')
            total = mgr.count()
            movies = mgr[start:start + size]

            return JsonResponse({"movies": [
                {"id": movie.id, "title": movie.title,'rate':movie.rate,'kind':movie.kind}
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

class MovieView11(View):
    def get(self, request):  # 方法名一定是小写
        try:
            page = vaildate(request.GET, 'page', 1, int, lambda x, y: x if x > 0 and x < 51 else y)
            size = vaildate(request.GET, 'size', 5, int, lambda x, y: x if x > 0 and x < 101 else y)

            start = size * (page - 1)
            mgr = AllMovies.objects.filter(kind__icontains='动画')
            total = mgr.count()
            movies = mgr[start:start + size]

            return JsonResponse({"movies": [
                {"id": movie.id, "title": movie.title,'rate':movie.rate,'kind':movie.kind}
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

class MovieView12(View):
    def get(self, request):  # 方法名一定是小写
        try:
            page = vaildate(request.GET, 'page', 1, int, lambda x, y: x if x > 0 and x < 51 else y)
            size = vaildate(request.GET, 'size', 5, int, lambda x, y: x if x > 0 and x < 101 else y)

            start = size * (page - 1)
            mgr = AllMovies.objects.filter(kind__icontains='喜剧')
            total = mgr.count()
            movies = mgr[start:start + size]

            return JsonResponse({"movies": [
                {"id": movie.id, "title": movie.title,'rate':movie.rate,'kind':movie.kind}
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
class MovieView13(View):
    def get(self, request):  # 方法名一定是小写
        try:
            page = vaildate(request.GET, 'page', 1, int, lambda x, y: x if x > 0 and x < 51 else y)
            size = vaildate(request.GET, 'size', 5, int, lambda x, y: x if x > 0 and x < 101 else y)

            start = size * (page - 1)
            mgr = AllMovies.objects.filter(kind__icontains='动作')
            total = mgr.count()
            movies = mgr[start:start + size]

            return JsonResponse({"movies": [
                {"id": movie.id, "title": movie.title,'rate':movie.rate,'kind':movie.kind}
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

class MovieView14(View):
    def get(self, request):  # 方法名一定是小写
        try:
            page = vaildate(request.GET, 'page', 1, int, lambda x, y: x if x > 0 and x < 51 else y)
            size = vaildate(request.GET, 'size', 5, int, lambda x, y: x if x > 0 and x < 101 else y)

            start = size * (page - 1)
            mgr = AllMovies.objects.filter(kind__icontains='爱情')
            total = mgr.count()
            movies = mgr[start:start + size]

            return JsonResponse({"movies": [
                {"id": movie.id, "title": movie.title,'rate':movie.rate,'kind':movie.kind}
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

class MovieView15(View):
    def get(self, request):  # 方法名一定是小写
        try:
            page = vaildate(request.GET, 'page', 1, int, lambda x, y: x if x > 0 and x < 51 else y)
            size = vaildate(request.GET, 'size', 5, int, lambda x, y: x if x > 0 and x < 101 else y)

            start = size * (page - 1)
            mgr = AllMovies.objects.filter(kind__icontains='科幻')
            total = mgr.count()
            movies = mgr[start:start + size]

            return JsonResponse({"movies": [
                {"id": movie.id, "title": movie.title,'rate':movie.rate,'kind':movie.kind}
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

class MovieView16(View):
    def get(self, request):  # 方法名一定是小写
        try:
            page = vaildate(request.GET, 'page', 1, int, lambda x, y: x if x > 0 and x < 51 else y)
            size = vaildate(request.GET, 'size', 5, int, lambda x, y: x if x > 0 and x < 101 else y)

            start = size * (page - 1)
            mgr = AllMovies.objects.filter(kind__icontains='奇幻')
            total = mgr.count()
            movies = mgr[start:start + size]

            return JsonResponse({"movies": [
                {"id": movie.id, "title": movie.title,'rate':movie.rate,'kind':movie.kind}
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

class MovieView17(View):
    def get(self, request):  # 方法名一定是小写
        try:
            page = vaildate(request.GET, 'page', 1, int, lambda x, y: x if x > 0 and x < 51 else y)
            size = vaildate(request.GET, 'size', 5, int, lambda x, y: x if x > 0 and x < 101 else y)

            start = size * (page - 1)
            mgr = AllMovies.objects.filter(kind__icontains='冒险')
            total = mgr.count()
            movies = mgr[start:start + size]

            return JsonResponse({"movies": [
                {"id": movie.id, "title": movie.title,'rate':movie.rate,'kind':movie.kind}
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
