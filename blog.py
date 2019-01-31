def corrector(name):
	#your code
	n=[]
	for i in name:
		if i.isupper():
			n.append(' ')
		n.append(i)

	print(''.join(n))
	return
title = str
titles = []

while title != '':
	title = input()
	titles.append(title)
	corrector(list(title))