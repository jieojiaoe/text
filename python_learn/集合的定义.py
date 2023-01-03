my_set = {"传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima"}
my_set_empty = set()    # 空集合定义
print(f"my_set的内容是:{my_set},类型是{type(my_set)}")
print(f"my_set_empty的内容是:{my_set_empty},类型是{type(my_set_empty)}")
# 集合无序，用bool()验证
my_set_empty = {"传智教育", "itheima", "黑马程序员"}
print(bool(my_set == my_set_empty))


