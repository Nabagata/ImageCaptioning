import numpy as np
import json
import csv
import glob, os
import pickle

train_part=np.load('train_part.npy')
[",".join(item) for item in train_part.astype(str)]
#test_part=np.load('test_part.npy')
#[",".join(item) for item in train_part.astype(str)]
c=0
#files = glob.glob('train/*.jpg')
#for file in files:
#	if file[34:] in train_part:
#		c=c+1
#	print(file[34:])
#print(c)

#for x in train_part:
#    # print(x.decode())
#	for file in files:
#		if x.decode() == file[34:]:
#			#os.rename("flickr30k_images/flickr30k_images/{}".format(file[34:]),"train/{}".format(file[34:]))
#			c=c+1

#for x in train_part:
#    # print(x.decode())
#	for file in files:
#		if x.decode() == file[34:]:
#			#os.rename("flickr30k_images/flickr30k_images/{}".format(file[34:]),"train/{}".format(file[34:]))
#			c=c+1


# csv file name
#filename = "results.csv"

## initializing the titles and rows list
#fields = []
#rows = []

## reading csv file
#with open(filename, 'r') as csvfile:
#    # creating a csv reader object
#    csvreader = csv.reader(csvfile)

#    # extracting field names through first row
#    fields = next(csvreader)

#    # extracting each data row one by one
#    for row in csvreader:
#        rows.append(row)

#    # get total number of rows
#    print("Total no. of rows: %d"%(csvreader.line_num))

## printing the field names
#print('Field names are:' + ', '.join(field for field in fields))

imagex = []
imagey = []

#print('\nrows are:\n')
#for row in rows:
#    # parsing each column of a row

#    for col in row:
##    	print('lol')
#    	array = col.split("|")
#    	imagex.append(array[0])
#    	imagex.append(array[0])
#    	imagex.append(array[0])
#    	imagex.append(array[0])
#    	imagex.append(array[0])
##    	imagey.append(array[2])
##    	for word in array:
##    		print(word)
#        array = col.split("|")
#	for word in array:
#		print(word)
    # print(col[0])
#	print('\n')

import csv

with open('results.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are {", ".join(row)}')
            line_count += 1
        else:
        	for x in train_part:
        		if x.decode() == row[0]:
#        			print(line_count)
#        			print('\t{} {} {}.'.format(row[0],row[1],row[2]))
#					temp = []
#					temp.append(row[2])
#					temp.append(row[2])
#					temp.append(row[2])
#					temp.append(row[2])
#					temp.append(row[2])
#        			imagex.append(row[0])
#        			imagex.append(row[0])
#        			imagex.append(row[0])
#        			imagex.append(row[0])
#        			imagex.append(row[0])
					imagey.append(row[2])
					imagex.append(row[0])
					line_count += 1
    print('Processed {} lines.'.format(line_count))    
    
#file_handler = open('images_pickle.dat', 'rb+')
#imagex, imagey = pickle.load(file_handler)
#file_handler.close()
file_handler = open('images_pickle.dat', 'wb+')
pickle.dump((imagex, imagey), file_handler)
file_handler.close()
#for i in imagex:
#	print(i)
#for i in imagey:
#	print(i)    
print(len(imagex))
print(len(imagey))
