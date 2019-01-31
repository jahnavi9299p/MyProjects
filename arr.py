def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('') 
    return
def max(it):
	m=0
	for x in it:
		if x>m:
			m=x
	print(m)
	return m
n = int(input())
arr = map(int, input().split())
#print_iterator(arr)
l=list(arr)
#print(l)
mm=max(l)
l.sort(reverse=True)
#print(l[::-1])
for i in l:
	if l[i]<mm
		print(l[i])
