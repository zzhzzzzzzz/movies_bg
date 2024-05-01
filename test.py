from lxml import etree
import requests
import pandas as pd

base_url = "https://movie.douban.com/chart"
headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
response=requests.get(base_url,headers=headers)

movie_urls=[]
with response:
    root = etree.HTML(response.text)
    title = root.xpath("//tr[@class='item']//a[@class='nbg']")
    for i in title:
        movie_urls.append(i.get('href'))


def collection_data(data=None,pakeage=[]):
    if len(data)==1:
        pakeage.append(data[0].strip())
    if len(data)>=2:
        string=""
        for item in data:
            item=item.strip()
            string=string+item+' / '
            if item==data[-1]:
                string=string+item
        pakeage.append(string)
    return pakeage


def get_info(list=None):
    movies_title, release_date, movies_rate, movie_kind , movie_time,movie_director,movie_actor,movie_location,movie_language=[], [], [], [], [],[],[],[],[]
    comment_user, movie_comment, comment_postline =  [],[],[]
    for i in range(len(list)):
        pakeage=[]
        url=list[i]
        response=requests.get(url,headers=headers)
        print("========================================")
        with response:
            root = etree.HTML(response.text)
            # 标题
            title = root.xpath("//div[@id='content']/h1//span[@property]/text()")
            print(*title)
            collection_data(title,movies_title)

            # 上映时间
            year= root.xpath("//div[@id='content']/h1//span[@class]/text()")
            print(*year)
            collection_data(year, release_date)

            # 豆瓣评分
            rate = root.xpath("//div[@id='content']//strong/text()")
            print(*rate)
            collection_data(rate, movies_rate)



            # 类别
            kind=root.xpath('//div[@id="info"]/span[@property="v:genre"]/text()')
            collection_data(kind, movie_kind)

            # 片长
            time=root.xpath('//div[@id="info"]/span[@property="v:runtime" ]/text()')
            collection_data(time,movie_time)

            # 导演
            director=root.xpath('//div[@id="info"]//a[@rel="v:directedBy"]/text()')
            collection_data(director, movie_director)

            #主演列表
            actor=root.xpath('//div[@id="info"]//span [@class="actor"]/span[@class="attrs"]//a[@rel="v:starring"]/text()')
            collection_data(actor,movie_actor)


            D=root.xpath("//*[@id='info']/text()")
            l=[]
            for i in D:
                i = i.strip()
                if len(i)>=2:
                    l.append(i)
            # 产地
            collection_data([l[0]],movie_location)
            print(l[0])
            # 语言
            collection_data([l[1]],movie_language)
            print((l[1]))





            # # 短评信息
            # # 用户名称
            # user=root.xpath('//span[@class ="comment-info"]/a/text()')
            # print([*user])
            # # 发表时间
            # postline=root.xpath('//span[@class ="comment-time "]/text()')
            # date_data=collection_data(postline, [])
            # print(date_data)
            # comment_postline.append(date_data)
            # # 发表地点
            # postlocation=root.xpath('//span[@class="comment-location"]/text()')
            # location_data = collection_data(postlocation, [])
            # print(location_data)
            # # 评论内容
            # comment = root.xpath('//span[@class="short"]/text()')
            # comment_data = collection_data(comment, [])
            # print(comment_data)
            # # movie_comment.append(comment)
    print(movies_title, release_date, movies_rate, movie_kind, movie_time, movie_director, movie_actor, movie_location, movie_language,sep="\n")
    for i in [movies_title, release_date, movies_rate, movie_kind, movie_time, movie_director, movie_actor, movie_location, movie_language]:
        print(len(i))
    dataframe = pd.DataFrame({
        "title": movies_title,
        "release_date": release_date,
        "rate": movies_rate,
        "kind":movie_kind,
        "country":movie_location,
        "language":movie_language,
        "time":movie_time,
        "director": movie_director,
        'actor':movie_actor

    })
    # 保存信息到本地
    dataframe.to_csv(r'C:\Users\Administrator\Desktop\123movies.csv',index=True,encoding='utf8')

get_info(movie_urls)
