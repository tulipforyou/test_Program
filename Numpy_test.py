"""numpy是高性能科学计算和数据分析的基础包
ndarray:一种多维数组对象"""
import numpy as np
np.set_printoptions(suppress=True)#禁止以科学计数法显示数据
import matplotlib.pyplot as plt

class Numpy_test:
    def __init__(self):
        pass

    def array_test(self):
        data1=np.arange(12,20)#返回一个范围的ndarray数组
        print("arange返回一个范围的ndarray数组:\n",data1)
        data2=[[23,3.2,-0.3,-6,500],[3.1,69,56,-69,-0.2]]
        arr1=np.array(data2) #将列表转换为ndarray数组
        print("将列表转换为ndarray数组:\n",arr1)
        print("数组类型为：\n",arr1.dtype)
        """ 强制类型转换(注意：调用astype会创建一个原数组的一份拷贝数组）"""
        arr1_change=arr1.astype(np.int32)
        print("强制类型转换:\n",arr1_change)
        print("强制类型转换后类型为:\n",arr1_change.dtype)
        arr2=np.ones_like(arr1)#根据指定类型和形状创建全1数组
        print("根据指定类型和形状创建全1数组:\n",arr2)
        arr3=np.eye(10) #创建指定正方NXN矩阵，对角线为1,其余全0
        print("创建指定正方NXN矩阵，对角线为1,其余全0:\n",arr3)
        arr4=np.array([[1,2,3.6,-0.9,-5],[5,6,9,8,8]])
        print("数组间的任何算术运算都会应用到元素级：\n")
        print("arr4:\n",arr4)
        print("arr4*arr4\n",arr4*arr4)
        print("arr4-arr4\n",arr4-arr4)
        print("数组的广播问题：\n")
        arr5=np.array([1,2,3,4,5,6,7,8,9,10])
        arr6=arr5[2:6]
        print("arr5为：\n",arr5)
        print("arr6是arr5的切片：\n",arr6)
        arr6[3]=456789
        print("改变原数组的切片后的变化：\n",arr5)
        print("布尔型索引：\n")
        boolArr1=np.array(['sch','why','xj','hjy'])
        boolArr2=np.random.randn(4,8)
        #plt.plot([0,3],[-3,3],boolArr2[0:])
        print("索引为boolArr1：\n",boolArr1)
        print("对应数据为boolArr2：\n",boolArr2)
        print("boolArr2[boolArr1=='sch']:\n",boolArr2[boolArr1=='sch'])
        print("boolArr2[boolArr1=='sch',5:]:\n", boolArr2[boolArr1 == 'sch',5:])
        x=np.linspace(-np.pi,np.pi,314,endpoint=True)#linspace产生范围和大小内随机数组
        plt.plot(np.sin(x))
        plt.show()


    if __name__=='__main__':
        array_test()
