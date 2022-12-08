# import requests
# r = requests.get('https://www.baidu.com') #http头一定要有，给到变量r
# print(r,type(r))
# print(r.status_code) #返回200，表示连接成功
# print(r.encoding) #http header中猜测的相应内容编码
# print(r.apparent_encoding) #通过真实内容源文件，去分析判断它的编码方式
#
# r.encoding = r.apparent_encoding
# #当不能通过encoding正常解码时（比如中文出现乱码）,通过这行代码，将读取内容时通过猜测得到的不可靠的的编码
# #方式，更改为通过真实内容解析出来的编码方式，用正确的编码方式就可以正常读取了
#
# print(r.text)
# #相当于文件里面的 r.read(),读取网页。

'''添加额外信息'''
# r1 = requests.get('http://httpbin.org/get?name=zhangsan&sex=man')
# print(r1.text)

# '''也可以以字典形式添加'''
# info = {'name':'Zhangsan',"sex":"male"}
# r2 = requests.get('http://httpbin.org/get',params=info)
# print(r2.text)
# print(type(r2.text)) #<class 'str'>
# print(r2.json()) #通过r.json()将网页返回数据转化为字典格式
# print(type(r2.json())) #<class 'dict'>

'''有些网站禁止爬虫爬取内容：例如：知乎发现'''
# head = {"User-Agent":"Mozilla/5.0"}
# r3=requests.get('http://www.zhihu.com/explore',headers = head)
# r3.encoding = r3.apparent_encoding
# print(r3.status_code)
# print(r3.text)
# fp = open('a.html','wb')
# fp.write(r3.content)
# fp.close()

'''Post请求：发送数据给服务器 requests.post()'''
##1.发送Data：提交字符信息

# data = 'hello world'
# r4 = requests.post('http://httpbin.org/post',data=data)
# print(r4.status_code)
# print(r4.text)

##2. 发送表单数据form：提交表单信息
# d = {'name':'wangwu','password':'198711'}
# r5 = requests.post('http://httpbin.org/post',data=d)
# print(r5.status_code)
# print(r5.text)

##3. files:文件上传
# file1={'file':open('a.txt','r')}
# r6=requests.post('http://httpbin.org/post',files=file1)
# print(r6.status_code)
# print(r6.text)
# fp = open('b.html','wb')
# fp.write(r6.content)
# fp.close()

'''高级用法Cookies'''
##爬取知乎
# head ={'Cookie':'_zap=d0fa91dc-62e2-4273-b168-4b2cfc41e20b; d_c0="ABCQx4QWthOPTn46RXB51i8Vkr6WFGJcf9Q=|1631417230"; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=H5%2BOROa2ewlABQRRABN6gq7DDlGxbSgT; _xsrf=MRSHlqOsh3WSGGinItb05eMjUpe6g9mG; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1651057200; SESSIONID=vI3uSO7n6mDo6JWUIe5ecKCI7C7aLX6I1mGSIz9EiCr; JOID=VFERBkMkuTlNyYlfVidYJ3V3AWZHXf0LNZTJZTkc23Aj8s0HDhaXXCzIi1Naxbt58JZZTGaUvUsFSY5nC3FtGr8=; osd=VFoRAEMksjlLyYlUViFYJ353B2ZHVv0NNZTCZT8c23sj9M0HBRaRXCzDi1VaxbB59pZZR2aSvUsOSYhnC3ptHL8=; __snaker__id=JU8F8BOaRBPflSjz; gdxidpyhxdE=Goln0y7Vb456SoVSu0pC9XiB%5Cv4axrRBccAQQ589%2BiqLEinqPUM5iT7WmNzHkAbeI5voyuBSQcuwr3i%2BLzd%5C55PDbTQKr%2BqG35b6PcSEZe7f1JRzLNkH%2BNxTrAsayafSbk2ktsPMKKhH%2B6fETRwnSHGEw5X2GohOi2sO8MiEPb7iDQSq%3A1651058101126; YD00517437729195%3AWM_NI=JhrbvNLOfYuZwwmybN37Ol5xLPPmgXEtfSUb29ERejMLjgw8t0%2FNbf%2FW%2BBdEGmX06FMfsnRwrRPUlrlOqPJ%2BjeT4nlH%2FTROnbhTqt0nC9cNEl6%2Ff3pw7Q%2BuPVvOag8R8SFQ%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee94b45486b7f894ee3ff58a8aa6d45f878b8f83c45a85b2ad8ee44595898384e12af0fea7c3b92a8ab8be83f5469091aabaf852b5a9a39ae146f1e9818db8749090a08ee65487acaab4d86af2e78bb3e8628f94a688f634b8f0e1afe16eed89e5a3e74f85b398d1b54e8fbabd8fd17db28ea0b6ef7ab091bfb1c921aabb9cd5ed688cf19cb3ce66a2b89c92f73cae9df784cd4fb0eae187b27cb5e99fccf85c96aa8182e63492e89da7d437e2a3; captcha_session_v2=2|1:0|10:1651057202|18:captcha_session_v2|88:Qlg5QnA1dGtQbmUxdUF6dFBaL1hIVjlzdEdHR2g4NzBaZGc2TjJ3SjVFNFQwKzI3VDNMajJtcms4UGoxdDJwdw==|03281db3869d8d6b2cb6a870843edb4953e57e26e646ddaaf4ee86dda7c022d3; captcha_ticket_v2=2|1:0|10:1651057212|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfSG9jaHJZS3hIb2cteEpBQ2EwUXhYSE12MkNBRjZRSEdiWEUubktOVUNwSjljUUJLSlJkUzVNSnYuNk1jODdDNGFXWEN0eGpOUkl6OHBPVzFuZngxQVdDRlZaQ0xtRG93ZV9ldG53QjZ2cUdvUXFzQUxKcUVhVUdFTzhWZkRTWWtjLlJKYTBZRU0tNUVLOFNJci5XNjU1VUlMUmw5WEhTUTVEcmVBQ1NwdWp6aE9fcm9abHlhMjAyTWd2UC5Ybi50VFpPN1dtXy5tYld0dXk1QWZ3TWh6R3cudUlqVC5pWm9FTl9MVzZfd0lpSVVHZUdzazEwRVB4MmxCLkx2WVVCOTk2U2o3a2JNMFhhaWJOalEtNVRQQ2ZuZTJ3bTR5UzR1aTlOMWR3UWVrUUFrck9kanBmS3gyMFh6eWJIZUNqYmVjTGFoMTZkYl9waFE0OHNYbS11OVpBMWItSVlrQl9ldDhqanVsRFdfS1EuemdzYS5UU29JamNLUUVKSWFoQS1GVzZ2Y1hsSVdpUVNHRVNtZWt5Ti1weDRmT1FmQlZtV3I0dWdfdFU1b2lNdUFsOTJXRTh2Zkh5Z1ZFQVFKYkMxc2drVzVuOEdGa1JJOThfZFlQNG1PUS1tNVBqU1VmRHVtdnBaZ3NDbzZrWXEyUHJNcUd6QWVudGM4NGhjMyJ9|1bab572549bf0b5701308b1f34112f8228aee48dea87c67ff56d444bc6cc5871; z_c0=2|1:0|10:1651057212|4:z_c0|92:Mi4xSkFpMkF3QUFBQUFBRUpESGhCYTJFeVlBQUFCZ0FsVk5QSEJXWXdEQm5xNnI1RXhBdGJCY2lHTTN6V09FWWthcmlB|f0b488c78b7439c8f0090f556f06098521c965f78459eef91ce60ac07a5eae24; q_c1=9ac8487320724764b7225356717da2b0|1651057213000|1651057213000; NOT_UNREGISTER_WAITING=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1651057221; tst=r; KLBRSID=57358d62405ef24305120316801fd92a|1651057310|1651057197',
# "User-Agent":"Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/"}
# r = requests.get('http://www.zhihu.com',headers=head)
# print(r.status_code)
# fp = open('c.html','wb')
# fp.write(r.content)
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key + '=' +value)

##爬取百度（百度上关于python的内容）
# head = {'cookie':'H_WISE_SIDS=107313_110085_127969_164870_174441_179350_184716_186635_188747_188843_189037_189755_189802_190621_190793_191068_191245_191287_192206_192391_192407_193283_193290_193559_194085_194520_195003_195189_195329_195342_195631_196045_196428_197002_197241_197288_197470_197471_197579_197711_197782_197829_197958_198034_198259_198470_198514_198649_198917_199082_199286_199305_199466_199571_199618_199753_199777_199797_200037_200159_200193_200272_200350_200450_200553_200597_200762_200959_201054_201107_201233_201328_201360_201445_201535_201556_201580_201700_201733_201889_201948_201979_202178_202284_202393_202476_202545_202554_202561_8000085_8000124_8000139_8000163_8000173_8000185_8000193; PSTM=1651194279; BD_HOME=1; BIDUPSID=F8979A782C76A45E0D6B926ECF18C544; BD_UPN=123253; BA_HECTOR=240l00a4a4a52080cb1h6med80q; BDUSS=lOWGRWbGtCanV4dVJhbDJOMnMwbFVGQXlQWWNQdDZoNElKfnNzTXA2SEd4cEppRVFBQUFBJCQAAAAAAAAAAAEAAABrg5GRU2hhacD1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMY5a2LGOWtiMV; BDUSS_BFESS=lOWGRWbGtCanV4dVJhbDJOMnMwbFVGQXlQWWNQdDZoNElKfnNzTXA2SEd4cEppRVFBQUFBJCQAAAAAAAAAAAEAAABrg5GRU2hhacD1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMY5a2LGOWtiMV; H_PS_PSSID=36309_31660_34813_36166_34584_35979_36339_36073_36265_26350_36312_36061; BAIDUID=FD0EF8F5DBC3C102745F192B900BF833:SL=0:NR=10:FG=1; sug=3; sugstore=0; ORIGIN=0; bdime=20100; BAIDUID_BFESS=FD0EF8F5DBC3C102745F192B900BF833:SL=0:NR=10:FG=1',"User-Agent":"Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/"}
# r = requests.get('http://www.baidu.com/s?w=java',headers=head)
# print(r.status_code)
# fp=open('d.html','wb')
# fp.write(r.content)
# fp.close()

'''模拟登陆Github网页，并爬取登陆状态后的setting页面'''
# import requests
# class Login(object):
#     #创建一个叫Login的类，定义属性
#     def __init__(self):
#         self.headers={'Referer': 'https://github.com/',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
#             'Host': 'github.com'}
#         self.login_url = 'https://github.com/login' #登陆的网址
#         self.post_url = 'https://github.com/session' #提交session的网页
#         self.logined_url = 'https://github.com/settings/profile' #登陆后要爬取的网址
#         self.session = requests.session() #会话维持
#
#     def au_to(self):
#         #authenticity——token
#         r = self.session.get(self.login_url,headers = self.headers)
#         print(r.status_code)
#         for line in r.text.split('\n'): #遍历登陆页面源代码,以\n（换行）来分割
#             if 'authenticity_token' in line:
#
#                 line_new = line.split('value=')[1].split('"')[1]
#                 #注意：（""，和'"'的区别，这里是后者，分开来看其实是' " '，以"进行分隔的意思）
#
#         return line_new #返回authenticity——token密钥
#
#     def login(self,id,password):
#         post_data = {
#             'commit': 'Sign in',
#             'authenticity_token': self.au_to(),
#             'ga_id': '2046617795.1581235169',
#             'login': id,  # 登陆的用户名
#             'password': password,  # 登陆的密码
#             'webauthn - support': 'supported',
#             'webauthn - iuvpaa - support': 'unsupported',
#             'timestamp': '1651847155330',        #需要修改
#             'timestamp_secret': '3aef40d40b8e3ec75d4a52d45469b6f1daa1144802483981e53fbd069f00ac5b' #需要修改
#         } #提交的表单数据（到网页上去找的）
#         response = self.session.post(self.post_url,data = post_data, headers = self.headers)
#         print(response.status_code)
#         fp = open('login.html','wb')
#         fp.write(response.content)
#         fp.close()
#
#         response1 = self.session.get(self.logined_url,data = post_data, headers = self.headers)
#         print(response1.status_code)
#         fp1 = open('logined.html','wb')
#         fp1.write(response1.content)
#         fp1.close()
#
# if __name__ == '__main__':
#     login = Login()
#     login.login(id='ShellyZSR',password='Shelly310919kcl')

'''代理服务器'''
import requests
proxie = {'http':'http://115.29.199.16:8118'} #代理服务器的类型，IP以及端口

r = requests.get('http://httpbin.org/get',proxies= proxie)
print(r.text)

#下面这个代码没有讲
# r = requests.get('https://www.taobao.com',proxies= proxies)
# print(r.status_code)
# print(r.headers)
# fp = open('proxies.html','wb')
# fp.write(r.content)
# fp.close()





























