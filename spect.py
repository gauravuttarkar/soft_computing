import csv

n = 23

def func (w, data, threshold,lr):
	sum = 0
	for i in range(len(data)):
		sum = sum + data[i] * w[i];

	sum = sum + w[-1]	 
	print(sum)
	res = None
	e = 0
	if ( sum >= threshold ):
		res = 1
	else:
		res = 0;

	if data[-1] - res:
		e = 1
	for i in range(len(w)):
		w[i] = w[i] + lr * ( data[-1] - res) * data[i] 
	return (w,e)

def test(w, data,threshold,lr):
	sum = 0
	for i in range(len(data)):
		sum = sum + data[i] * w[i];

	sum = sum + w[-1]
	if ( sum >= threshold ):
		res = 1
	else:
		res = 0;

	print("error is ", data[-1] - res )	
	return data[-1] - res

data = []

with open('SPECT.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	i = 0

	for row in reader:
		# print(row)
		list1=[]

		for i in range(1,23):
			list1.append(float(row['Attr_'+str(i)]))		
		
		if row['Class'] == 'Yes':
			list1.append(1)
		else:
			list1.append(0)

		data.append(list1)	

threshold = 2
lr = 0.2
init_weight = 1 / n
iterate = 5000

w = []

for i in range(n):
	w.append(init_weight)

print(w)

ten_fold = 0

flag = 0

while(ten_fold<10):
	print('*'*50)
	for j in range(iterate):
		for i in data[:ten_fold+int(267*0.9)]:
			w,e = func(w,i,threshold,lr)
			flag = e
		if flag == 0:
			for i in data[:int(267*0.9)]:
				w,e = func(w,i,threshold,lr)
			if e == 0:
				break

				

	print('Testing')
	for i in data[int(267*0.9):]:
		test(w,i,threshold,lr)
	for i in data[:268-int(267*0.9)]	:
		test(w,i,threshold,lr)
	ten_fold = ten_fold + 1
count = 0
flag = 0
for i in data:
	count = count + 1
	e = test(w,i,threshold,lr)
	flag = e
if flag == 0:
	print('Test Successful for ',count,"cases")
else:
	print('Test failed')	

print(w)		
