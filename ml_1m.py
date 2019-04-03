import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json
import requests

# 文本请求
"""url = 'http://www.baidu.com'
r = requests.get(url)
with open('test.txt', 'w') as f:
    f.write(r.text)"""
#获取四个数据
def getUsers():
    user_names=['user_id','gender','age','occupation','zip']
    users=pd.read_csv('ml-1m/users.dat',sep='::',header=None,names=user_names,engine='python')
    return users
def getRating():
    rating_names=['user_id','movie_id','rating','timestamp']
    ratings=pd.read_csv('ml-1m/ratings.dat',sep='::',header=None,names=rating_names,engine='python')
    return ratings
def getMovies():
    movie_names=['movie_id','title','genres']
    movies=pd.read_csv('ml-1m/movies.txt',sep='::',header=None,names=movie_names,engine='python')
    return movies
#验证数据是否成功提取
def testData():
    print('This is users message:\n',getUsers())
    print('This is ratings message:\n',getRating())
    print('This is movies message:\n',getMovies())
def dataOperation():
    data=pd.merge(pd.merge(getRating(),getUsers()),getMovies())#三个表进行合并
    mean_ratings=data.pivot_table('rating',index='title',columns='gender')
    #print(mean_ratings[:5])
    ratingByTitle=data.groupby('title').size()
    #print(ratingByTitle[:10])
    activeMovie=ratingByTitle.index[ratingByTitle>=250]   #大于250条评论的分组
    mean_ratings=mean_ratings.ix[activeMovie]      #mean_ratings已经是评论大于250条的数据了
    #print(mean_ratings[:10])
    topFemaleRating=mean_ratings.sort_values(by='F',ascending=False)#对女性评分电影降序排列
    #print('对女性评分电影降序排列:\n',topFemaleRating[:10])
    mean_ratings['diff']=mean_ratings['M']-mean_ratings['F']  #新增列DIFF为男女评分差值
    sortedByDiff=mean_ratings.sort_values(by='diff')
    #print(sortedByDiff[:10])
    manLoveMovie=sortedByDiff[::-1]#对排序结果反序，即可得男性喜爱的电影
    #print(manLoveMovie[:15])