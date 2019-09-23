import numpy as np
import cv2
# from matplotlib import pyplot as plt

def readimg():
    # filename：文件路径
    # flags=None：读取方式
    # cv2.IMREAD_COLOR：读入一副彩色图像。图像的透明度会被忽略，这是默认参数。
    # cv2.IMREAD_GRAYSCALE：以灰度模式读入图像
    img = cv2.imread('last.png',0)
    cv2.namedWindow('myimage', cv2.WINDOW_NORMAL)
    cv2.imshow('myimage',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('mywrite.png',img)

# def readvideo():
#     cap = cv2.VideoCapture(0)
#     while (True):  # Capture frame-by-frame
#         ret, frame = cap.read() # Our operations on the frame come here
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# Display the resulting frame
#         cv2.imshow('frame', gray)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break # When everything done, release the capture
#     cap.release()
#     cv2.destroyAllWindows()

def readvideo():
    cap = cv2.VideoCapture(0)# Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')#编码格式
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))#播放频率。帧大小，isColor TRUE彩色，false灰色
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame, 0) # write the flipped frame
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        else:
            break# Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def matchimg():
    img = cv2.imread('last.png', 0)
    img2 = img.copy()
    template = cv2.imread('temp_player.jpg', 0)
    w, h = template.shape[::-1]
    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    for meth in methods:
        img = img2.copy()
    # exec 语句用来执行储存在字符串或文件中的 Python 语句。
    # 例如，我们可以在运行时生成一个包含 Python 代码的字符串，然后使用 exec 语句执行这些语句。
    # eval 语句用来计算存储在字符串中的有效 Python 表达式
        method = eval(meth)
    # Apply template Matching
        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)#最小值，最大值，最小值索引,最大值索引
    # 使用不同的比较方法，对结果的解释不同
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        # 参数说明：img表示图片，(x, y)表示矩阵左上角的位置，(x+w, y+h)表示矩阵右下角的位置, (0, 0, 255)表示颜色，2表示线条

        # 画矩形
        # 第一个参数：img是原图
        # 第二个参数：（x，y）是矩阵的左上点坐标
        # 第三个参数：（x + w，y + h）是矩阵的右下点坐标
        # 第四个参数：（0, 255, 0）是画线对应的rgb颜色
        # 第五个参数：2 是所画的线的宽度
        cv2.rectangle(img2, top_left, bottom_right, (0, 0, 255), 2)
        # 显示出来
        name=meth + str('_rec')
        cv2.namedWindow(name, cv2.WINDOW_NORMAL)
        # cv2.namedWindow(meth + str('_rec'), cv2.WINDOW_NORMAL)
        cv2.imshow(name, img2)

    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__=="__main__":
    # readimg()
    # readvideo()
    # img = cv2.imread('first.jpg', 0)
    # print(img.shape)#行数/hegih，列数/width
    # 通道数：注意：如果图像是灰度图，返回值仅有行数和列数。所以通过检查这个返回值就可以知道加载的是灰度图还是彩色图
    # print(img.size)#可以返回图像的像素数目
    #OpenCV 将颜色读取为 BGR（蓝绿色红色）
    matchimg()