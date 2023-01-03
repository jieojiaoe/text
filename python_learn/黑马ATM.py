money = 5000000
name = input("请输入你的账户姓名：")
i = None


def query_balance_function(number1):
    print(f"{name}，您好，你的余额剩余：{money}元")


def deposit_function(number2):
    number2 = int(input("请输入金额："))
    global money
    money += number2
    print(f"{name}，您好，您存款{number2}元成功")
    print(f"{name}，您好，你的余额剩余：{money}元")


def withdrawal_function(number3):
    number3 = int(input("请输入金额："))
    global money
    money -= number3
    print(f"{name}，您好，您取款{number3}元成功")
    print(f"{name}，您好，你的余额剩余：{money}元")


def main_menu_function():
    global i
    i = int(input(f'''---------------主菜单---------------
    {name}，你好，欢迎来到黑马银行ATM。请选择操作：
    查询余额      【输入1】
    存款          【输入2】
    取款          【输入3】
    退出          【输入4】
    请输入您的选择：'''))


main_menu_function()
while 0 < 1:
    if i == 1:
        query_balance_function(5122)
        i == int(input("请输入接下来的操作："))
    elif i == 2:
        deposit_function()
        i == int(input("请输入接下来的操作："))
    elif i == 3:
        withdrawal_function()
        i == int(input("请输入接下来的操作："))
    elif i == 4:
        break
    else:
        break

