# 9.4 turtle库
# import turtle
#一、窗体函数
# turtle.setup(width, height, startx, starty);需要与turtle.done()进行配合
#1。width：窗口宽度，如果值是整数，表示的像素值；如果值是小数，表示窗口宽度与屏幕的比例
#2。height：窗口高度，如果值是整数，表示的像素值；如果值是小数，表示窗口高度与屏幕的比例；
#3。startx:窗口左侧与屏幕左侧的像素距离，如果值是None，窗口位于屏幕水平中央；
#4. starty:窗口顶部与屏幕顶部的像素距离，如果值是None，窗口位于屏幕垂直中央；


#二、画笔运动函数
# 1.turtle.forward()：沿着当前方向前进指定距离
# 2. turtle.backward():沿着当前相反方向后退指定距离 (方向不变)
# turtle.setup()
# turtle.forward(200) #简写: turtle.fd()
# turtle.backward(400)  #简写: turtle.bk()
# turtle.done()

#3. turtle.right(angle): 向右旋转angle角度
#4.turtle.left(angle): 向左旋转angle角度
#5.turtle.setheading(angle):设置当前朝向为angle角度（通过坐标轴）
# turtle.setup()
# turtle.right(90)
# turtle.forward(200)
# turtle.left(90)
# turtle.forward(200)
# turtle.setheading(150) #简写：turtle.seth()
# turtle.forward(200)
# turtle.done()

#6.turtle.goto(x,y):移动到绝对坐标（x,y）处
# turtle.setup()
# turtle.goto(100,100)
# turtle.goto(100,-100)
# turtle.done()

#7.turtle.circle(radius,e):绘制一个指定半径r和角度e的圆或弧形
# turtle.setup()
# turtle.circle(100,360)
# turtle.undo()
# turtle.done()

#8.turtle.undo():撤销画笔最后一步动作 (详见上）

#9. turtle.speed():设置画笔的绘制速度，参数为0-10之间
# turtle.setup()
# turtle.speed(10)
# turtle.forward(200)
# turtle.done()

#turtle库实例：绘制多边形（例子是六边形）
# import turtle
# turtle.setup()
# for i in range(20):
#     turtle.setheading(i*(360/20))
#     turtle.forward(20)
# turtle.done()

#三、画笔状态函数
#1、turtle.penup()：提起画笔
#  turtle.pendown()：放下画笔
import time
import turtle
turtle.setup()
# turtle.penup() #提起画笔
# turtle.forward(200) #画笔提着向前走200像素，画笔移动，但没有画到纸上任何东西
# turtle.pendown() #画笔落下
# turtle.circle(20,300) #开始画半径20像素，300度弧
# turtle.done()


#2、turtle.pensize(width)：设置画笔线条的粗细为指定大小
# turtle.pensize(10) #画笔10像素
# turtle.fd(200)
# turtle.pensize(1)
# turtle.fd(200)
# turtle.done()

#3. turtle.color(): 设置画笔的颜色
# turtle.color('purple')
# turtle.fd(200)
# turtle.done()

#4. turtle.begin_fill():填充图形前，调用该方法
#   turtle.end_fill():填充图形结束
#两行代码需一起使用，才能实现填充颜色的功能
# turtle.begin_fill()
# turtle.color('purple')
# turtle.circle(50,360)
# print(turtle.filling()) #True
# turtle.end_fill()
# print(turtle.filling()) #False,在end_fill()代码之后，已经end_fill了，所以是未填充
# turtle.done()
#5. turtle.filling(): 返回填充的状态，True为填充，False为未填充


#6. turtle.clear(): 清空当前窗口，但不改变当前画笔的位置(小海龟位置还留在当前位置不变）
# turtle.fd(200)
# turtle.color('pink')
# turtle.circle(50,360)
# # turtle.clear()
# #7.turtle.reset():清空当前窗口，并重置位置等状态为默认值
# turtle.reset() #(画笔颜色变回黑色，小海龟也回到远点)
# turtle.done()

#8. turtle.screensize():设置画布的长和宽
# turtle.fd(300)
# turtle.screensize(800,800) #可以出现滚动条
# turtle.done()

#9. turtle.hideturtle(): 隐藏画笔的turtle形状
turtle.fd(50)
turtle.hideturtle()
print(turtle.isvisible()) #False
#10.showturtle():显示画笔的turtle形状
time.sleep(2)
turtle.showturtle()
print(turtle.isvisible()) #True
turtle.done()
#11.turtle.isvisible():如果turtle可见，则返回True