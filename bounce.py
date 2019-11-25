"""Bounce, a simple animation demo.

Exercises

1. Make the ball speed up and down.
2. Change how the ball bounces when it hits a wall.
3. Make the ball leave a trail.
4. Change the ball color based on position.
   Hint: colormode(255); color(0, 100, 200)

"""

from random import *
from turtle import *
from freegames import vector

def value():
    "Randomly generate value between (-5, -3) or (3, 5)."#使产生的值在这两个数之间
    return (3 + random() * 2) * choice([1, -1])#这样操作可以使数在这之间

ball = vector(0, 0)#定义这个二维向量
aim = vector(value(), value())#随机生成范围之内的向量

def draw():
    "Move ball and draw game."#使球移动起来并绘制游戏
    ball.move(aim)#使球运动起来

    x = ball.x#把球的横坐标赋值给x
    y = ball.y#把球的纵坐标赋值给y

    if x < -200 or x > 200:#使得球的横坐标不超出屏幕
        aim.x = -aim.x#使球运动改变方向


    if y < -200 or y > 200:#使得球的纵坐标不超出屏幕
        aim.y = -aim.y#使球运动改变方向

    clear()
    goto(x, y)#让它到达坐标系的指定位置
    dot(10)#绘制一份指点直径的圆点

    ontimer(draw, 50)#用来控制刷新时间

setup(420, 420, 370, 0)#设置窗体大小
hideturtle()#隐藏箭头显示
tracer(False)#绘制开始之前调用，直接给用户显示绘制结果
up()#抬起画笔，之后，移动画笔不绘制形状
draw()#调用函数
done()#停止画笔绘制，但绘图窗口不关闭
#不是很明白为什么把窗体设为420，如果400不是更好吗
