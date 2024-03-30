def B(datalist, Kh, Ih):
    '''
    compute the value of B
    '''
    Blist = []
    for uh in datalist:
        b = round(uh*1000/(Kh*Ih), 2)
        Blist.append(b)
    return Blist

def addList(list1, list2):
    '''
    add the value of list element by the order of lists
    '''
    list3 = []
    for i in range(len(list1)-1):
        e = round(list1[i] + list2[i], 2)
        list3.append(e)
    return list3

#input your labdata
dataList1 = [1.27, 1.86, 2.40, 3.10, 3.78, 4.08, 3.86, 3.27, 2.58, 1.99, 1.53, 1.17, 0.88, 0.66, 0.50, 0.37]
dataList2 = [0.37, 0.49, 0.66, 0.88, 1.17, 1.56, 2.05, 2.69, 3.36, 3.91, 4.01, 3.61, 2.87, 2.17, 1.57, 1.13]
dataList3 = [1.54, 2.10, 2.89, 3.79, 4.73, 5.36, 5.60, 5.63, 5.64, 5.64, 5.78, 5.65, 5.65, 5.60, 5.23, 5.43, 3.54, 2.64, 1.94, 1.43]

#input your Kh, Ih
Kh = 1141 #unit V*A(-1)*T(-1)
Ih = 2.5  #unit mA

Blist1 = B(dataList1, Kh, Ih)
Blist2 = B(dataList2, Kh, Ih)
Blist3 = B(dataList3, Kh, Ih)
Blist4 = addList(Blist1, Blist2)

message1 = "测量亥姆霍兹线圈左线圈单独通电时轴线上的磁场：" + "\n" + str(Blist1)
message2 = "测量亥姆霍兹线圈右线圈单独通电时轴线上的磁场：" + "\n" + str(Blist2)
message3 = "测量亥姆霍兹线圈左右线圈同时通电时轴线上的磁场：" + "\n" + str(Blist3)
message4 = "左右相加：" + "\n" + str(Blist4)

print(message1)
print(message2)
print(message3)
print(message4)