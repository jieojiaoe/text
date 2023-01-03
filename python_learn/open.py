import time
f = open("E:/ceshi.txt", "r", encoding="UTF-8")
# print(type(f))
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是：{line1}")
# print(f"第二行数据是：{line2}")
# print(f"第三行数据是：{line3}")

for line in f:
    print(f"每一行数据是：{line}")
    


