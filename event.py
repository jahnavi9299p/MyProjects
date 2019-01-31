import csv

eve={1:'CS',2:'GoogleIt',3:'TreasureHunt'}
lis=[]
def new():
	name=input('Enter Name: ')
	e=int(input('Select Event-\n1.CS\t2.GoogleIt\t3.TreasureHunt\n'))
	lis.append([name.title(),eve[e]])
	with open('event.csv', 'a', newline='') as csvfile:
		spamwriter = csv.writer(csvfile)
		spamwriter.writerow([name.title()] + [eve[e]])

def view():
	with open('event.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			print(': '.join(row))

def choice():
	n=int(input('\nWhat would you like to do?\n1.Add Participant\n2.See Participants\n'))
	if n==1:
		new()
	elif n==2:
		view()
	else:
		exit()

inp=str
while inp!='':
	choice()

