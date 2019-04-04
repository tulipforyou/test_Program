import pandas as pd
import public_function
# 文本请求
"""url = 'http://www.baidu.com'
r = requests.get(url)
with open('test.txt', 'w') as f:
    f.write(r.text)"""
#获取四个数据
def getUsers():
    print("begining to get users's message......")
    user_names=['user_id','gender','age','occupation','zip']
    users=pd.read_csv('ml-1m/users.dat',sep='::',header=None,names=user_names,engine='python')
    with open('data.txt','a') as f:
        f.write("\nusers's message:\n")
        f.write(str(users))
    print("the users's message has got!!!")
    return users
def getRating():
    print("begining to get rating's message......")
    rating_names=['user_id','movie_id','rating','timestamp']
    ratings=pd.read_csv('ml-1m/ratings.dat',sep='::',header=None,names=rating_names,engine='python')
    with open('data.txt','a') as f:
        f.write("\nrating's message:\n")
        f.write(str(ratings))
    print("the rating's message has got!!!")
    return ratings
def getMovies():
    print("begining to get movies's message......")
    movie_names=['movie_id','title','genres']
    movies=pd.read_csv('ml-1m/movies.txt',sep='::',header=None,names=movie_names,engine='python')
    with open('data.txt','a') as f:
        f.write('\nmovies\'s message:\n')
        f.write(str(movies))
    print("the movies's message has got!!!")
    return movies
#验证数据是否成功提取
@public_function.gettime
def testData():
    print("begining to test data......")
    print('This is users message:\n',getUsers())
    print('This is ratings message:\n',getRating())
    print('This is movies message:\n',getMovies())
    print("test successful!!!")

@public_function.gettime
def dataOperation():
    testData()
    print("the table is setting......")
    data=pd.merge(pd.merge(getRating(),getUsers()),getMovies())#三个表进行合并
    mean_ratings=data.pivot_table('rating',index='title',columns='gender')
    #print(mean_ratings[:5])
    ratingByTitle=data.groupby('title').size()
    #print(ratingByTitle[:10])
    activeMovie=ratingByTitle.index[ratingByTitle>=250]   #大于250条评论的分组
    mean_ratings=mean_ratings.ix[activeMovie]      #mean_ratings已经是评论大于250条的数据了
    #print(mean_ratings[:10])
    topFemaleRating=mean_ratings.sort_values(by='F',ascending=False)#c
    with open('data.txt','a') as f:
        f.write('\n对女性评分电影降序排列(输出前10个）:\n')
        f.write(str(topFemaleRating[:10]))
    print('对女性评分电影降序排列(输出前10个）:\n',topFemaleRating[:10])
    mean_ratings['diff']=mean_ratings['M']-mean_ratings['F']  #新增列DIFF为男女评分差值
    sortedByDiff=mean_ratings.sort_values(by='diff')
    with open('data.txt','a') as f:
        f.write("\n男性和女性对同一电影评分差值（输出前10个）：\n")
        f.write(str(sortedByDiff[:10]))
    print("男性和女性对同一电影评分差值（输出前10个）：\n",sortedByDiff[:10])
    manLoveMovie=sortedByDiff[::-1]#对排序结果反序，即可得男性喜爱的电影
    with open('data.txt','a') as f:
        f.write("\n男性喜爱电影排名（输出前15个）\n")
        f.write(str(manLoveMovie[:15]))
    print("男性喜爱电影排名（输出前15个）\n",manLoveMovie[:15])
if __name__=='__main__':
    getUsers()
    getRating()
    getMovies()
    testData()
    dataOperation()