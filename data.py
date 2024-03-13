import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['axes.unicode_minus']=False

def analyse(item):
    file=pd.read_csv(r"C:\Users\Administrator\Desktop\allmovies.csv",header=0,encoding='utf8')
    pd.DataFrame(file)
    data=file[item]
    c_ls=[]
    c_dic={}
    for i in data:
        if '/' in i:
            for j in i.split('/'):
                c_ls.append(j.strip())
        if '/' not in i:
            for j in i.split():
                c_ls.append(j.strip())
    for x in c_ls:
        c_dic[x]=c_dic.get(x,0)+1
    return c_dic

def data(c_dic):
    ls=[]
    for i in c_dic.items():
        d={}
        d['value']=i[1]
        d['name']=i[0]
        ls.append(d)
    return ls

c_dic=analyse('kind')
data=data(c_dic)
print(data)