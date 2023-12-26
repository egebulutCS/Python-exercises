alist=[]
q="y"
while q=="y" or q=="Y":
	n=int(input("Enter a number to add to the list:"))
	alist.append(n)
	q=input("Would you like to add another number to the list?[Y/N]")
b=-1
while -b!=len(alist):
	if len(alist)==0:
		break
	if alist[b]<alist[b-1]:
		temp=alist[b-1]
		alist[b-1]=alist[b]
		alist[b]=temp
		b=-1
	else:
		b-=1
print(alist)
k=input("Press enter to exit")