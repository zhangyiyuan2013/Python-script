
import random          # 导入random模块
for i in range(3):     # 使用for循环重复执行3次
    rule = {'布': 0, '剪刀': 1, '石头': 2}  # 创建一个rule字典

    rand_res = random.randint(0, 2)      # 调用random.randint函数
    input_s = input('输入石头、剪刀、布：')   # 让客户输入石头、剪刀、布
    input_res = rule[input_s]
    win = True

    if abs(rand_res - input_res) == 2:  # 相差2说明是布和石头相遇，出布一方胜
        if rand_res == 0:
            win = False
    elif rand_res > input_res:  # 相差1的情况谁大谁赢
        win = False

    print(f'程序出：{list(rule.keys())[rand_res]}，输入：{input_res}')

    if rand_res == input_res:
        print('平')
    else:
        print('赢' if win else '输')
