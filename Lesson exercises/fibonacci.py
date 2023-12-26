list1=[1,1]
counter=2
n=int(input("How many numbers would you like to see?"))
while counter<n:
	a=list1[-1]+list1[-2]
	counter+=1
	list1.append(a)
print(list1)
k=input("Press enter to exit")