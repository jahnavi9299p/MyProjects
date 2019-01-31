import csv
dire={}
i=3
while i!=0:
	name=input('Enter Name: ')
	usn=input('Enter USN: ')
	dire[usn]=name
	with open('direc.csv', 'a', newline='') as csvfile:
		spamwriter = csv.writer(csvfile)
		spamwriter.writerow([usn] + [name.title()])
	i-=1

with open('direc.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			print(': '.join(row))