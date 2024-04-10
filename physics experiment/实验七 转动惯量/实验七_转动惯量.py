def computeAlpha(list1, list2):
    alphaList = []
    for i in range(len(list1)):
        t1 = list1[i]
        t2 = list2[i]
        # print(t1)
        # print(t2)
        alpha_raw = 2*pi*(N1*t2 - N2*t1)/(t1*t1*t2 - t2*t2*t1)
        alpha = round(alpha_raw, 3)
        alphaList.append(alpha)
    
    return alphaList

def computeAlphaAver(alphaList):
    alphaAverList = []
    for i in range(len(alphaList)):
        if (i%3 == 0):
            alphaSum = alphaList[i] + alphaList[i+1] + alphaList[i+2]
            alphaAver = round(alphaSum/3, 3)
            alphaAverList.append(alphaAver)

    return alphaAverList

def computeJ1(alphaAverList):
    JList = []
    for i in range(0, 4, 2):
        alpha_true = alphaAverList[i] + alphaAverList[i+1]
        J_raw = Moment/alpha_true
        J = round(J_raw, 5)
        JList.append(J)

    return JList

def computeJ2(alphaAverList):
    JList = []
    for i in range(4, 8, 2):
        alpha_true = alphaAverList[i] + alphaAverList[i+1]
        J_raw = Moment/alpha_true
        J = round(J_raw, 5)
        JList.append(J)

    return JList

def analyze(Jx, J_ideal):
    Error_percent = round(abs(Jx - J_ideal)/J_ideal*100, 2)
    return Error_percent

#引入pi
import math
pi = math.pi 

#预置圈数
N1 = 2
N2 = 6

#实验数据（SI制）
m = 34.4/1000   #砝码质量
g = 9.794       #重力加速度
r = 2.50/100    #转轴半径
Moment = m*g*r  #外力矩
M = 419.16/1000 #铝盘质量
r1 = 10/100     #铝盘内半径
r2 = 11.96/100  #铝盘外半径
m_c = 165.6/1000#一个圆柱质量
d = 3/100       #圆柱移动的距离

#时间t1(左 -> 右)
time_list1 = [1.370, 1.466, 1.316, 
              0.871, 0.881, 0.843,
              3.572, 2.436, 3.728,
              1.110, 1.137, 1.102,
              1.872, 2.551, 1.837,
              0.944, 0.920, 0.941,
              1.946, 2.721, 2.240,
              0.966, 1.009, 0.989]

#时间t2(左 -> 右)
time_list2 = [3.244, 3.399, 3.152,
              2.631, 2.661, 2.544,
              6.834, 5.270, 6.303,
              3.349, 3.433, 3.324,
              4.177, 5.060, 4.127,
              2.852, 2.776, 2.842,
              4.311, 5.259, 4.714,
              2.919, 3.050, 2.989]

alphaList = computeAlpha(time_list1, time_list2)
alphaAverList = computeAlphaAver(alphaList)

JList_raw1 = computeJ1(alphaAverList)
Jx1 = round((JList_raw1[1] - JList_raw1[0]), 5)
J_ideal1 = round(1/2*M*(r1*r1 + r2*r2), 5)
Error_percent1 = analyze(Jx1, J_ideal1)

JList_raw2 = computeJ2(alphaAverList)
Jx2 = round((JList_raw2[1] - JList_raw2[0]), 5)
J_ideal2 = round(2*m_c*d*d, 5)
Error_percent2 = analyze(Jx2, J_ideal2)


print("角加速度为：")
print(alphaList)
print("角加速度平均值为：")
print(alphaAverList)
print("1.测定圆环的转动惯量")
print("承物台和全系统的转动惯量分别为：")
print(JList_raw1)
print("它们的差即为物体转动惯量：" + "\n" + str(Jx1))
print("理想转动惯量为：" + "\n" + str(J_ideal1))
print("误差为：" + str(Error_percent1) + "%")
print("2.验证平行轴定理")
print("两次转动惯量J1和J2为：")
print(JList_raw2)
print("它们的差为：" + "\n" + str(Jx2))
print("理想转动惯量为：" + "\n" + str(J_ideal2))
