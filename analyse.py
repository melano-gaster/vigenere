#!/usr/bin/env python3 
import sys



def monoanalyser(ss=int):
	seq = ''
	for i in range(subseqNo):
		seq += (task[ss][i])

	for j in range(subseqNo , len(task[ss])):
		if seq in db[ss].keys() :
			db[ss][seq] += 1
		else:
			db[ss][seq] = 1
		seq += task[ss][j]
		seq = seq[1:]

	tag = [(i , db[ss][i]) for i in db[ss].keys() ]
	tag.sort(reverse= True , key=lambda x : x[1])
	return tag



if len(sys.argv) < 3:
	print("Usage: \n\t analyse.py filename key_length seq_length")
	sys.exit(0)
elif len(sys.argv) == 3:
	try:
		key_length = int(sys.argv[2])
		subseqNo = 1
	except:
		print('last argument must be a number!')
		sys.exit(0)

	try:
		with open(sys.argv[1]) as f:
			cfile = f.readlines()
	except IOError:
		print("file is missing")
		sys.exit(0)
else:
	print("too many arguments")
	sys.exit(0)

db = [dict() for i in range(key_length)]
#print(db)
test = "XRIPH RRGIA QZQLH MBEMX XMYYM CKPJR XNMRH YXRIP"

print(cfile)
test = ''.join(cfile)
test = test.replace(' ', '')
test = test.replace('\n' , '')
task = [[j for c , j in enumerate(test) if (c % key_length == i)] for i in range(key_length)]


for k in range(key_length):
	print("****",k+1,"****")
	for i in monoanalyser(k):
		print(i[0] ,':', i[1])



