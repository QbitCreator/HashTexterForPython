import random
import math
import hashlib


def sha256(cleartext):
        result=hashlib.sha256((cleartext).encode()).hexdigest()
        return result

def hashlistcreator(password, layers):
	hashcache=password
	hashlist=[]
	for i in range(layers):
		hashcache=sha256(hashcache)
		hashlist.append(hashcache)
	return hashlist

def encrypt(password, data):
	data=list(str.encode(data))
	size=len(data)
	layers=math.ceil(math.log(size, 64))
	salt=""
	for i in range(32):
		salt+=chr(random.randint(48,127))
	hashlist=hashlistcreator(password+salt, layers)
	basehashbytes=list(str.encode(sha256(hashlist[len(hashlist)-1])))
	for n in range(len(data)):
		current=data[n]
		data[n]=(current+(basehashbytes)[n%64])%255
	for i in range(len(hashlist)):
		x=hashlist[i]
		datablockscache=[[]]
		b=0
		for c in range(len(data)):
			y=data[c]
			if len(datablockscache[b]) < 64**(layers-i):
				datablockscache[b].append(y)
			else:
				datablockscache.append([])
				b+=1
				datablockscache[b].append(y)
		for n in range(len(datablockscache)):
			current=datablockscache[n]
			for m in range(len(current)):
				character=current[m]
				datablockscache[n][m]=(character+(list(str.encode(x))[n%64]))%255
				datablockscache[n][m]=(datablockscache[n][m]+(list(str.encode(hashlist[(i+1)%len(hashlist)])))[n%64])%255
		datablockscache = [element for sublist in datablockscache for element in sublist]
		data=datablockscache
	result=salt+" "
	for x in data:
		cryptchar=str(hex(x)[2:])
		if len(cryptchar)==1:
			cryptchar="0"+cryptchar
		result+=cryptchar
	return result

def decrypt(password, data):
	data=data.split()
	salt=data[0]
	data=data.pop(1)
	data=[data[idx:idx + 2] for idx in range(0, len(data), 2)]
	for i in range(len(data)):
		d=data[i]
		data[i]=int(d, 16)
	size=len(data)
	layers=math.ceil(math.log(size, 64))
	hashlist=hashlistcreator(password+salt, layers)
	hashlist.reverse()
	for i in range(len(hashlist)):
		x=hashlist[i]
		datablockscache=[[]]
		b=0
		for c in range(len(data)):
			y=data[c]
			if len(datablockscache[b]) < 64**(i+1):
				datablockscache[b].append(y)
			else:
				datablockscache.append([])
				b+=1
				datablockscache[b].append(y)
		for n in range(len(datablockscache)):
			current=datablockscache[n]
			for m in range(len(current)):
				character=current[m]
				datablockscache[n][m]=datablockscache[n][m]-(list(str.encode(x)))[n%64]-(list(str.encode(hashlist[(i+len(hashlist)-1)%len(hashlist)])))[n%64]
				if datablockscache[n][m]<0:	
					datablockscache[n][m]=255+datablockscache[n][m]
		datablockscache = [element for sublist in datablockscache for element in sublist]
		data=datablockscache
	basehashbytes=list(str.encode(sha256(hashlist[0])))
	for n in range(len(data)):
		current=data[n]      
		data[n]=current-basehashbytes[n%64]
		if data[n]<0:
			data[n]=255+data[n]
	passwordcheck=0
	result=""
	for c in data:
		if (c<0 or c>127):
			passwordcheck+=1
		else:
			result+=chr(c)
	if passwordcheck==0:
		return result
	else:
		return "ERROR: Wrong password!"
