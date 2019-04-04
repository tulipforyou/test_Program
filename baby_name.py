import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def dataFound():  #获取数据
#提取1880年出生孩子信息
    names1880=pd.read_csv('names/yob1880.txt',names=['name','sex','births'])
    #print(names1880.groupby(by='sex').births.sum())#分组求和
    pieces=[]
    years=range(1880,2011)
    columns=['name','sex','births']
    for year in years:  #所有文件汇总为一个文件
        path='names/yob%d.txt' % year
        frame=pd.read_csv(path,names=columns)
        frame['year']=year
        pieces.append(frame)  #加入YEAR列，表示年份
    """将所有数据组成的列表整合为单个DataFrame表格
    必须要指定ignore_index=True，因为我们不希望保留read_csv所返回的原始行号"""
    names=pd.concat(pieces,ignore_index=True)
    #print(names)
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
    #print(names)
    """如果按YEAR和SEX排列，后面将不能对生成的数据按YEAR和SEX排列"""
    grouped=names.groupby(['births'])
    #print(grouped)
    top_1000=grouped.apply(getTop1000)
    #print(top_1000)
    return top_1000

def get_quantile_count(group,q=0.5):
    group=group.sort_values(by='prop',ascending=False).prop.cumsum()
    return group.searchsorted(q)+1

def name_analyse():#命名分析
    People=dataCreat()
    bays=People[People.sex=='M']   #man
    girls=People[People.sex=='F']  #female
    #按TEAR和NAME统计的总出生数透视表
    totle_people=People.pivot_table('births',index='year',columns='name',aggfunc=sum)
    #按指定名字画图
    subset=totle_people[['John','Harry','Mary','Linda','Marilyn']]
    subset.plot(subplots=True,figsize=(10,10),grid=False,title="Number of births per year")
    #按比例绘图
    table=People.pivot_table('prop',index='year',columns='sex',aggfunc=sum)
    #X轴步长为10,Y轴最大值为1.2,最小值为0,其间分12份
    table.plot(xticks=range(1880,2020,10),yticks=np.linspace(0,1.2,13), title="Number of births per year by prop")
    #对所需百分值的人数索引求值
    diversity=People.groupby(['year','sex']).apply(get_quantile_count)
    diversity=diversity.unstack('sex')
    diversity.plot(title="Number of popular names in top 50%")
    print("关闭当前图表以显示其他图表！！！")
    plt.show()

def theLastLetterChange():  #最后一个字母的变革
    names=dataCreat()
    get_last_letter=lambda x:x[-1]
    last_letters=names.name.map(get_last_letter)
    last_letters.name='last_letter'
    table=names.pivot_table('births',index=last_letters,columns=['sex','year'],aggfunc=sum)
    subtable=table.reindex(columns=[1910,1960,2010],level='year')
    letter_prop=subtable/subtable.sum().astype(float) #求当前年份每个字母占当前年份总人数比例
    # 3为生成图表数量，FIGSIZE为窗口尺寸
    fig,axes=plt.subplots(2,1,figsize=(10,10))
    letter_prop['M'].plot(kind='bar',rot=0,ax=axes[0],title='Male')
    letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female',legend=False)
    #最后一个字母以指定字母结尾
    letter_prop1=table/table.sum().astype(float)
    dny_end=letter_prop1.ix[['d','n','y'],'M'].T
    dny_end.plot(title='the last letter of end with d or n or y of male')
    #变性名字
    all_names=names.name.unique()
    mask=np.array(['lesl' in x.lower() for x in all_names])
    lessly_like=all_names[mask]
    filtered=names[names.name.isin(lessly_like)]
    table=filtered.pivot_table('births',index='year',columns='sex',aggfunc='sum')
    table=table.div(table.sum(1),axis=0)
    table.plot(style={'M':'k-','F':'k--'},title=U"begin with lesl and the sex is changing")
    plt.show()

if __name__=='__main__':
    dataFound()
    dataCreat()
    name_analyse()
    theLastLetterChange()

