vec = [[1,2,3], [4,5,6], [7,8,9]]
num = []
'''
for elem in vec:
	for num_ in elem:
		num.append(num_)
'''
num = [num for elem in vec for num in elem]
for elem in num:
    print(elem)