number = int(input("请输入一个数字，能帮你找到1到该数的偶数个数："))
count = 0
for x in range(1, number):
    if x % 2 == 0:
        count += 1
print(count)
