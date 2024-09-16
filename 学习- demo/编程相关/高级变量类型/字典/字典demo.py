xiaoming = {'name': '小明',
            'age': 18,
            'gender': True,
            'height': 1.75}
print(type(xiaoming))

print(xiaoming['name'])
print(xiaoming.get('address'))
print(len(xiaoming))
print(xiaoming.keys())
print(xiaoming.values())
print(xiaoming.items())
print(xiaoming['name'])
print(xiaoming.get('name'))
# del xiaoming['gender']
# print(xiaoming)
# 要删除的值,前面加print指打印要删除的值
# xiaoming.pop('gender')
# print(xiaoming)
# 随机删除,前面加print指打印随机删除的值
# xiaoming.popitem()
# print(xiaoming)
# xiaoming.clear()
# print(xiaoming)
# xiaoming['age'] = 20
# print(xiaoming)
# xiaoming['tizhong'] = '1T'
# print(xiaoming)
# xiaoming.setdefault('love','xiaomei')
# print(xiaoming)
# 字典2的key不能与字典1冲突,否则不生效
# xiaomei = {'n': 'xiaomei',
#            'a': 16,
#            'tz': '200T'}
# xiaoming.update(xiaomei)
# print(xiaoming)

# for k, v in xiaoming.items():
#     print(k,v)

for k in xiaoming:
    print('%s: %s' % (k,xiaoming[k]))