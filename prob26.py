lis=[]
def add_word(w):
	lis.append(w)
s=str
while s!='':
	s=input('Enter the word ')
	add_word(s)
print(lis)