import matplotlib.pyplot as plt

def imgshow():
    img=plt.imread('1.png')
    plt.figure("Image")#图像窗口名称
    plt.imshow(img)
    plt.title('sch')#图像题目
    plt.axis('on')#是否显示坐标轴
    plt.show()

if __name__=='__main__':
    imgshow()