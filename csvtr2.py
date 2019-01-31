import csv
with open('eggs.csv', newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
      for row in spamreader:
          print(', '.join(row))
 #spamreader contains all the lines of the csvfile,
 # with each line forming a list