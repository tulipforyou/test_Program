import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def dataFound():  #获取数据
#提取1880年出生孩子信息
    names1880=pd.read_csv('names/yob1880.txt',names=['name','sex','births'])
    #print(names1880.groupby(by='sex').births.sum())#分组求和
    pieces=[]
    years=range(1880,1883)
    columns=['name','sex','births']
    for year in years:  #所有文件汇总为一个文件
        path='names/yob%d.txt' % year
        frame=pd.read_csv(path,names=columns)
        frame['year']=year
        pieces.append(frame)  #加入YEAR列，表示年份
    """将所有数据组成的列表整合为单个DataFrame表格
    必须要指定ignore_index=True，因为我们不希望保留read_csv所返回的原始行号"""
    names=pd.concat(pieces,ignore_index=True)
    return names

def add_prop(group): #求指定婴儿名字占总人数的比例
    births=group.births.astype(float)
    group['prop']=births/births.sum()
    return group

def getTop1000(group):#获取指定数量数据
    return group.sort_values(by='births',ascending=False)[:1000]

def dataCreat(): #生成数据集
    names=dataFound()
    #对每年出生总人数按行为年份，列为性别，进行求和输出
    #totlePeople=names.pivot_table('births',index='year',columns='sex',aggfunc=sum)
    #print(totlePeople.tail())
    names=names.groupby(['year','sex']).apply(add_prop)
    grouped=names.groupby(['sex'])
    top_1000=grouped.apply(getTop1000)
    #print(top_1000)
    return top_1000

def name_analyse():#命名分析
    People=dataCreat()
    bays=People[People.sex=='M']   #man
    girls=People[People.sex=='F']  #female
    #按TEAR和NAME统计的总出生数透视表
    totle_people=People.pivot_table('births',index='year',columns='name',aggfunc=sum)
    #按指定名字画图
    subset=totle_people[['John','Harry','Mary','Lon']]
    #subset.plot(subplots=True,figsize=(10,10),grid=False,title="Number of births per year")
    #按比例绘图
    table=People.pivot_table('prop',index='year',columns='sex',aggfunc=sum)
    table.plot(xticks=range(1880,1883,1),yticks=np.linspace(0,0.3,13), title="Number of births per year by prop")
    plt.show()