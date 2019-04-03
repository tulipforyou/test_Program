"""
    这是梦开始的地方！
    愿所有努力都不被辜负！
"""
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

user_names=['user_id','gender','age','occupation','zip']
users=pd.read_csv('ml-1m/users.dat',sep='::',header=None,names=user_names,engine='python')
rating_names=['user_id','movie_id','rating','timestamp']
ratings=pd.read_csv('ml-1m/ratings.dat',sep='::',header=None,names=rating_names,engine='python')
movie_names=['movie_id','title','genres']
movies=pd.read_csv('ml-1m/movies.txt',sep='::',header=None,names=movie_names,engine='python')
#验证数据是否成功提取
"""print('This is users message:\n',users[:5])
print('This is ratings message:\n',ratings[:5])
print('This is movies message:\n',movies[:5])"""

data=pd.merge(pd.merge(ratings,users),movies)#三个表进行合并
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
print(manLoveMovie[:15])