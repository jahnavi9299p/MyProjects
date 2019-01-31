#n=input('Enter the string:\n')
#di={}
#for i in n:
#	c=n.count(i)
#	di[i]=c
#print(di)

x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
k1=x.keys()
k2=y.keys()
lis=[]
for i in k1:
	for j in k2:
		if x[i]==y[j]:
			lis.append(x[i])

print(lis)