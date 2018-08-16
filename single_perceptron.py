import csv


data = []

n = 5


def func (w, data, threshold,lr):
	# for i in range(len(w)):
	# 	if i == 0:
	# print(data)
	# print(w)
	# print(threshold)
	sum = 0
	for i in range(len(data)):
		sum = sum + data[i] * w[i];

	sum = sum + w[-1]	 
	#print(sum)
	res = None
	e = 0
	if ( sum >= threshold ):
		res = 1
	else:
		res = 0;
	#print("data ",data[-1],"res ",res)
	
	#print("error is ", data[-1] - res )
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

def iteration():
	pass


with open('IRIS (1).csv') as csvfile:
	reader = csv.DictReader(csvfile)
	i = 0

	for row in reader:
		list1=[]

		list1.append(float(row['sepal length']))
		list1.append(float(row['sepal width']))
		list1.append(float(row['petal length']))
		list1.append(float(row['petal width']))
		if row['class'] == "Iris-versicolor":
			list1.append(1)
		else:
			list1.append(0)		
		data.append(list1)

	#print(row['first_name'], row['last_name'])
# for i in data:
# 	print(i)	

threshold = 0.9
lr = 0.4
init_weight = 1 / n

w = []

for i in range(n):
	w.append(init_weight)

# for i in data:
# 	print(i)

print(w)

ten_fold = 0

flag = 0

while(ten_fold<10):
	print('*'*50)
	for j in range(5000):
		for i in data[:ten_fold+90]:
			w,e = func(w,i,threshold,lr)
			flag = e
		if flag == 0:
			for i in data[:ten_fold+90]:
				w,e = func(w,i,threshold,lr)
			if e == 0:
				break

				

	print('Testing')
	for i in data[ten_fold+90:]:
		test(w,i,threshold,lr)
	for i in data[:101-ten_fold-90]	:
		test(w,i,threshold,lr)
	ten_fold = ten_fold + 1

flag = 0
for i in data:
	e = test(w,i,threshold,lr)
	flag = e
if flag == 0:
	print('Test Successful')
else:
	print('Test failed')		

print(w)

