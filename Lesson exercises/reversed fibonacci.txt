list1=[1,1]
counter=2
n=int(input("How many numbers would you like to see?"))
while counter<n:
	a=list1[-1]+list1[-2]
	counter+=1
	list1.append(a)
list1.reverse()
print(list1)
b=-1
while -b!=len(list1):
	if list1[b]<list1[b-1]:
		temp=list1[b-1]
		list1[b-1]=list1[b]
		list1[b]=temp
		b=-1
	else:
		b-=1
print(list1)
k=input("Press enter to exit")