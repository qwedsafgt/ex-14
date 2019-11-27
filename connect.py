"""Connect Four

Exercises

1. Change the colors.
2. Draw squares instead of circles for open spaces.
3. Add logic to detect a full row.
4. Create a random computer player.
5. How would you detect a winner?

"""

from turtle import *#导入画图模块
from freegames import line#从freegames模块中导入line函数

turns = {'red': 'yellow', 'yellow': 'red'}#创建一个颜色字典
state = {'player': 'yellow', 'rows': [0] * 8}#

def grid():
    "Draw Connect Four grid."
    bgcolor('light blue')#可以让我们将整个绘制屏幕调成任意颜色

    for x in range(-150, 200, 50):#循环（-150，200），每隔50
        line(x, -200, x, 200)#绘制一个线段

    for x in range(-175, 200, 50):#进行一个嵌套循环
        for y in range(-175, 200, 50):
            up()#抬起画笔，之后，移动画笔不绘制形状
            goto(x, y)#让它到达坐标系的指定位置
            dot(40, 'white')#绘制直径为四十，背景为白色的圆

    update()#不懂什么意思

def tap(x, y):#感应用户输入
    "Draw red or yellow circle in tapped row."
    player = state['player']#将yellow赋值给player
    rows = state['rows']#将元素为八个零的列表赋值给rows
    print(rows)
    row = int((x + 200) // 50)#将数制转换为整数
    count = rows[row]#将列表中顺序为row的数的元素赋值给count
    print(count)
    x = ((x + 200) // 50) * 50 - 200 + 25#算出对应的横向哪一个圆点
    y = count * 50 - 200 + 25#算出纵向对应哪一个圆点

    up()#抬起画笔，之后，移动画笔不绘制形状
    goto(x, y)#让他到达坐标系的指定位置
    dot(40, player)#绘制直径为40的圆点，用制定色黄色
    update()#不太懂

    rows[row] = count + 1#改变列表元素
    state['player'] = turns[player]#改变颜色列表元素，使用户每绘制一次就换一次颜色

setup(420, 420, 370, 0)#设置窗体大小
hideturtle()#隐藏箭头显示
tracer(False)#绘制开始之前调用，直接给用户显示绘制结果
grid()#调用grid函数，绘制带圆形的表格
onscreenclick(tap)#用来相应用户输入
done()#
