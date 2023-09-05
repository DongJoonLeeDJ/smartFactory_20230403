import csv

f = open('mydata.csv', 'r')

rdr = csv.reader(f)

isStart = True # 첫 줄은 읽지 않는다.

mydatas = []

for line in rdr:
	if isStart:
		isStart=False
		pass
	else:
		mydatas.append(line)
		
#for item in mydatas:
#	print(item)
f.close()
for item in mydatas:
	print( ('상호명:%s, 전화번호:%s, 대표메뉴:%s') % (item[1],item[3],item[4]) )