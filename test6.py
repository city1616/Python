# lambda

x = lambda a : a + 10
y = lambda a, b : a * b


print(x(5))
print(y(5, 6))

def myfunc(n):
	return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

s = "  "
if s.isalpha():
	print("ggg")
else:
	print("none")
print(s)
print(s.upper())
print(s.isalpha())
print(s)

a = 1234
tmp = list()
a1 = str(a)
for i in a1:
	tmp.append(int(i))
print(a1)
print(tmp)

for i in range(3, -1, -1):
	print(i)

phone = "123456789"
print(phone[-4:])