def corrector(n):
	#your code
	nm=[]
	print(n)
	for nam in n:
		nm=[]
		for name in nam:
			if name.isalpha() or name==' ':
				nm.append(name)
		print((''.join(nm)).title())
	return
name = str
names = []

while name != '':
	name = input()
	names.append(name.strip())


corrector(names)