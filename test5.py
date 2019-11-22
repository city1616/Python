#dictionary

dic = {'name' : 'pey', 'phone' : '01022213213', 'birth' : '1123'}
e = {}
d = set()
f = dict()

a = " Hello, World! "
print(a)
print(a.strip())

print(type(e))
print(type(d))
print(type(f))
print(dic)
print(dic.keys())
print(list(dic.keys()))
print(dic.values())
print(dic.items())
print(list(dic.items()))
print(dic['name'])
print(dic['phone'])
print(dic['birth'])
print(dic.get('name'))

for k in dic.keys():
	print(k)


a1 = 2
b1 = 500
if a1 < b1 : print("a < b")
print("a") if a1 > b1 else print("b")

a2 = 220
b2 = 220
print("a") if a2 > b2 else print("=") if a2 == b2 else print("b")

# num = num / 2 if num % 2 == 0 else num * 3 + 1