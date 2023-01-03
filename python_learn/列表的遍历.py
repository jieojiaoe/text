"""
演示对list列表的循环，使用while和for循环2种方式
"""


def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    mylist = ["传智教育", "黑马程序员", "Python"]
    # 循环控制变量通过下标索引来控制，默认0
    # 每次循环将下标索引变量加1
    # 循环条件：下标索引变量<列表的元素数量
    index = 0
    while index < len(mylist):
        # 通过index变量取出对应下标的元素
        element = mylist[index]
        print(f"列表的元素：{element}")
        index += 1


def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return:None
    """
    mylist = [1, 2, 3, 4, 5]
    for element in mylist:
        print(f"列表的元素：{element}")


list_while_func()
list_for_func()
