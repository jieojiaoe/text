# 1.定义这个列表，并用变量接受它，内容是：[21, 25, 21, 23, 22, 20]
mylist = [21, 25, 21, 23, 22, 20]
# 2.追加一个数字31，到列表的尾部
mylist.append(31)
# 3.追加一个新列表[29, 33, 30]，到列表的尾部
mylist.extend([29, 33, 30])
# 4.取出第一个元素（应是21）
num1 = mylist[0]
print(num1)
# 5.取出最后一个元素（应是30）
num2 = mylist[-1]
print(num2)
# 6. 查找元素31，在列表的下标
index = mylist.index(31)
print(index)
