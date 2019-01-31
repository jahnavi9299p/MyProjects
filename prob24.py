k={1:"Speckbit", 2:"World", 3:"Quiet"}
#for i in k.keys():
#	print("{}--{}".format(i,k[i]))
s=input('Search Element: ')
for i in k.keys():
	if k.get(i)==s:
		print(f"Key is {i}")