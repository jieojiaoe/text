"""
演示for循环的基础语法
"""
# for循环也被成为：遍历循环
number = 0
name = "itheima is a brand of itcast"
for x in name:
    if x == "a":
        number += 1
print(f"{name}中共含有：{number}个字母a")
