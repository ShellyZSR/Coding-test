#6.6 字典的操作函数
# 1。len(d) 字典d的元素个数（长度）一个键值对为一个元素
d= {'201801':'Shelly', "201802": "Merry", "201803": "Tony"}
print(len(d))  #3

# 2.min(d) 字典d中 键 的最小值 (键为字符串的话，将会判断unicode的值）
# max(d)  字典d中 键 的最大值
print(min(d))
print(max(d))
# 201801
# 201803

# 3. dict() 生成一个空字典 等同于{}
d1 = dict()
print(d1)
d2={}
print(d2)

#4 d.keys() 返回所有的键信息
# 返回结果是Python的一种内部数据类型dict_keys，专用于表示字典的键。
# 如果希望更好的使用返回结果，可以将其转换为列表list类型。
print(d.keys()) #dict_keys(['201801', '201802', '201803'])
print(list(d.keys())) #['201801', '201802', '201803']可供用户使用

#5。 d.values() 返回所有的值信息
# 返回字典中的所有值信息，返回结果是Python的一种内部数据类型dict_values
# 如果希望更好的使用返回结果，可以将其转换为列表类型。
print(d.values()) #dict_values(['Shelly', 'Merry', 'Tony'])
print(list(d.values())) #['Shelly', 'Merry', 'Tony']

#6. d.items() 返回所有的键值对
# 返回字典中的所有键值对信息，返回结果是Python的一种内部数据类型dict_items
print(d.items())
#dict_items([('201801', 'Shelly'), ('201802', 'Merry'), ('201803', 'Tony')])
print(list(d.items())) #返回的数据是元组类型
# [('201801', 'Shelly'), ('201802', 'Merry'), ('201803', 'Tony')]

#7 d.get(key, default) 键存在则返回相应值，否则返回默认值
# （查找某key，有则返回对应值value，没有则返回默认值default）
print(d.get("201801","没有该元素")) #Shelly
print(d.get("201807","没有该元素")) #没有该元素
print(d.get("201807")) #None
#注意：第二个元素default可以省略，如果省略则默认值为空。

#8 d.pop(key, default) 键存在则返回相应值，同时删除键值对，否则返回默认值。
# 第二个元素default可以省略，如果省略则默认值为空。
# 相比d.get()方法，d.pop()在取出相应值后，将从字典中删除对应的键值对。
print(d.pop("201801","没有该元素" ))
print(d)
# Shelly
# {'201802': 'Merry', '201803': 'Tony'}

#9. d.popitem() 随机从字典中取出一个键值对，以元组(key, value)形式返回,取出后从字典中删除这个键值对。
#注意：d.popitem()，括号里没有数据。它是随机删除
d3={'201901':'Shelly', "201902": "Merry", "201903": "Tony","201904": "Teresa"}
print(d3.popitem())  #('201904', 'Teresa')
print(d3) #{'201901': 'Shelly', '201902': 'Merry', '201903': 'Tony'}

#10. d.clear() 删除所有的键值对, 返回空的{}
# print(d.clear())  None
d.clear()
print(d)  # {}

#11 如果希望删除字典中某一个元素， 可以使用Python保留字del
# del d["key"] 中括号里为想要删除的元素所对应的键
d4 = {'2018011':'Shelly', "2018021": "Merry", "2018031": "Tony","2018041": "Teresa"}
del d4["2018021"]
print(d4)

#12 字典类型也支持保留字in，用来判断一个键是否在字典中。
# 如果在则返回True，否则返回False。
# 注意：只能判断一个键key是否在字典中，无法判断值value是否在字典中。
print("2018011" in d4)  #True
print("2018021" in d4)  #False

#13 字典可以遍历循环对其元素进行遍历:
# for x in dictionary:
#     语句块
for x in d4:
    print("字典d4的键和值分别是{}和{}".format(x,d4.get(x)))
#for循环返回的变量名是字典的索引值。
# 如果需要获得键对应的值，可以在语句块中通过get()方法获得












