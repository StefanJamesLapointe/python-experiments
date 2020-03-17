from random import random
n = 0
a = 0.9
b = 0.6
c = (b - 1) / (a + b - 2)
if random() < c:
	n = 0
else:
	n = 1
list = []
for i in range(200):
	x = random()
	if n == 0:
		if x < a:
			n = 0
		else:
			n = 1
	else:
		if x < b:
			n = 0
		else:
			n = 1
	list.append(n)
print(list)
