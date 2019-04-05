"""numpy是高性能科学计算和数据分析的基础包
ndarray:一种多维数组对象"""
import numpy as np
np.set_printoptions(suppress=True)#禁止以科学计数法显示数据

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


    if __name__=='__main__':
        array_test()
