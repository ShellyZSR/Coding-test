#9.2 time库
# 一、时间处理
import time
#1.time.time() : 获取当前时间戳。代表着如今的时间与1970年1月1日0时0分0秒的时间差(以秒为单位)
#可用来统计运行一个项目需要多长时间

# start_time = time.time() #运行该程序前的时间戳
# a = 0
# for i in range(100000000):
#     a += 1
# print(a)
# fin_time = time.time() #运行该程序后的时间戳
# print(fin_time-start_time) #二者相减，得出运行该程序所需时长
# #100000000
# 9.26442003250122

#2。time.gmtime(secs)：获取当前时间戳对应的struct_time对象,注意：是UTC时间
# time1=time.gmtime()
# print(time1)

#3。time.localtime(secs)：获取当前时间戳对应的本地时间的struct_time对象。
# print(time.localtime())

#4.time.ctime(secs): 获取当前时间戳对应的易读字符串表示，内部会调用time.localtime()函数以输出当地时间。
# print(time.ctime())
# Wed Mar 23 19:25:29 2022

#二、时间格式化
#1. time.mktime(t):函数将struct_time对象t转换为时间戳，注意t代表当地时间。
# import time
# t = time.localtime()
# print(t)
# print(time.mktime(t))
# time.struct_time(tm_year=2022, tm_mon=3, tm_mday=23, tm_hour=20, tm_min=56, tm_sec=38, tm_wday=2, tm_yday=82, tm_isdst=0)
# 1648040198.0

#2. time.strftime():该方法利用一个格式字符串，对时间格式进行表达。函数是时间格式化最有效的方法，
# 几乎可以以任何通用格式输出时间
# t = time.localtime()
# print(t)
# print(time.strftime('%Y-%m-%d %H:%M:%S',t)) #想要输出什么格式，就输入什么格式
# # 2022-03-23 21:00:20

#3. time.strptime(): 与strftime()方法完全相反，用于提取字符串中时间来生成strut_time对象，
# 可以很灵活的作为time模块的输入接口
# timestring = '2022-03-23 21:00:20'
# a = time.strptime(timestring,'%Y-%m-%d %H:%M:%S')
# print(a) #输出为struct_time格式的timestring。

#三、程序计时
#1。time. sleep()： 推迟调用线程的运行，可通过参数secs指秒数（括号里参数），表示进程挂起(睡眠)的时间
# import time
# start_time=time.time()
# time.sleep(2) #睡眠2秒钟
# fin_time = time.time()
# print(fin_time-start_time)

#2。time. perf_counter()：返回一个性能计数器的值(在分秒内)，即一个具有最高可用分辨率的时钟，以测量短时间。
# 比 time.time()更精确，二者精度是一样的，但相比perf_counter()可以测量更短的时间
# import time
# a1 = time.perf_counter()
# b1 = time.time()
# time.sleep(1)
# a2 = time.perf_counter()
# b2 = time.time()
# print('perf_counter起始时间：',a1,'结束时间：',a2,'间距：',a2-a1)
# print('time.time起始时间：',b1,'结束时间：',b2,'间距：',b2-b1)

#3.time库综合应用实例：模拟进度条显示
import time
scale = 50
start_time = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = "." * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter()-start_time
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end = '')
    time.sleep(0.2)
print('\n-------程序执行结束')