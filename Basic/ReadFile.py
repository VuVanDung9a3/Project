#fp = open("list.txt", "a")
#for line in fp:
#	print(line, end = '')
#fp.close
#print(fp.read())
#fp.write('Python ll')
BUFFERSIZE = 25000
f = open("big.txt", "r")
fp = open("list.txt", "w")
buffer = f.read(BUFFERSIZE)
i = 0
while (len(buffer)):
	i += 1
	fp.write(buffer)
	print(i, "{} byte".format(len(buffer)))
	buffer = f.read(BUFFERSIZE)
print('done')
