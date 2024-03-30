def compute_B(datalist, Kh, Ih):
    return [(uh*1000)/(Kh*Ih) for uh in datalist]

def add_list(list1, list2):
    return [round(e1 + e2, 2) for e1, e2 in zip(list1, list2)]

def create_list(data):
    return [round(float(i), 2) for i in data.split(', ')]

print('输入数据（用‘, ’）分隔' + '\n')

try:
    Kh = int(input('请输入Kh大小（单位：V*A^-1*T^-1）:'))
    Ih = float(input('请输入Ih大小（单位：mA）:'))
except:
    raise ValueError

data_tube = input("测量螺线管轴线上的磁场：")
data_left = input("测量亥姆霍兹线圈左线圈单独通电时轴线上的磁场：")
data_right = input("测量亥姆霍兹线圈右线圈单独通电时轴线上的磁场：")
data_both = input("测量亥姆霍兹线圈左右线圈同时通电时轴线上的磁场：")

data = [data_tube, data_left, data_right, data_both]
methods = {'B':compute_B, 'add_list':add_list, 'create_list':create_list}

data_list = [methods['create_list'](i) for i in data]
B_list = [methods['B'](i, Kh, Ih) for i in data_list]
B_leftAddright = methods['add_list'](B_list[1], B_list[2])

print('轴线：' + ', '.join(['{:.2f}'.format(x) for x in B_list[0]]))
print('左：' + ', '.join(['{:.2f}'.format(x) for x in B_list[1]]))
print('右：' + ', '.join(['{:.2f}'.format(x) for x in B_list[2]]))
print('同时：' + ', '.join(['{:.2f}'.format(x) for x in B_list[3]]))
print('左加右：' + str(B_leftAddright))
