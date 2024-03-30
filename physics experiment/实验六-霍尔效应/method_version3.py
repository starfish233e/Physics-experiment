def compute_B(datalist, Kh, Ih):
    '''
    compute the value of B
    '''
    return [(uh*1000)/(Kh*Ih) for uh in datalist]

def add_list(list1, list2):
    return [round(e1 + e2, 2) for e1, e2 in zip(list1, list2)]

#input your data
Kh = 1141
Ih = 2.5
data_tube = []
data_left = []
data_right = []

list_tube = compute_B(data_tube, Kh, Ih)
list_left = compute_B(data_left, Kh, Ih)
list_right = compute_B(data_right, Kh, Ih)
list_add = add_list(data_left, data_right)

message1 = "测量亥姆霍兹线圈左线圈单独通电时轴线上的磁场：" + "\n" + str(list_tube)
message2 = "测量亥姆霍兹线圈右线圈单独通电时轴线上的磁场：" + "\n" + str(list_left)
message3 = "测量亥姆霍兹线圈左右线圈同时通电时轴线上的磁场：" + "\n" + str(list_right)
message4 = "左右相加：" + "\n" + str(list_add)

print(message1)
print(message2)
print(message3)
print(message4)