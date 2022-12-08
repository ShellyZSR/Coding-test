#7.1文件的打开和关闭

#内置函数open()可以用指定模式打开指定文件并创建文件
# 变量名= open(文件路径及文件名，模式)
#1 open(文件路径及文件名，'r') 只读模式
f = open('/Users/teresa624/Documents/Coding/Python中文网课（淘宝凡博）/a.docx','r')
#2 open(文件路径及文件名，'w') 覆盖写模式：文件不存在则创建，存在则完全覆盖源文件
f = open('/Users/teresa624/Documents/Coding/Python中文网课（淘宝凡博）/b.docx','w')
#之前文件夹里没有b.docx，通过'w'创建一个新的b.docx文件,有则完全覆盖源文件

#3 open(文件路径及文件名，'x')创建写模式: 文件不存在则创建，存在则返回异常FileExistsError
f = open('/Users/teresa624/Documents/Coding/Python中文网课（淘宝凡博）/a.docx','x')

#4 open(文件路径及文件名，'a')追加写模式: 文件不存在则创建，存在则在原文件最后追加内容
f = open('/Users/teresa624/Documents/Coding/Python中文网课（淘宝凡博）/a.docx','a')
f.write('人工智能') #（写入信息）

#5 open(文件路径及文件名，'r+')与r/w/x/a一同使用，在原功能基础上增加同时读写功能
f = open('/Users/teresa624/Documents/Coding/Python中文网课（淘宝凡博）/a.docx','r+')

#文件使用结束后要用close()方法关闭，释放文件的使用授权
#变量名.close() 注意：变量名必须是open赋值的变量名
f.close()