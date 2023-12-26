import math, random
counter=0
numbers=[]
signs=[]
deck=[]
spades=[]
clubs=[]
diamonds=[]
hearts=[]
while counter<13:
	sign=random.randint(1,4)
	number=random.randint(1,13)
	i=0
	while i<counter:
		if numbers[i]!=number or signs[i]!=sign:
			i+=1
		else:
			break
	if i==counter:
		numbers.append(number)
		signs.append(sign)
		counter+=1
i=0
while i<13:
        if signs[i]==1:
                spades.append(numbers[i])
        elif signs[i]==2:
                hearts.append(numbers[i])
        elif signs[i]==3:
                clubs.append(numbers[i])
        elif signs[i]==4:
                diamonds.append(numbers[i])
        i+=1
n=1
while n<=4:
	if n==1:
		string=spades
	elif n==2:
		string=hearts
	elif n==3:
		string=clubs
	elif n==4:
		string=diamonds
	b=-1
	while -b!=len(string):
		if len(string)==0:
			break
		if string[b]<string[b-1]:
			temp=string[b-1]
			string[b-1]=string[b]
			string[b]=temp
			b=-1
		else:
			b-=1
	n+=1
a=" of Spades"
z=0
while z<13:
	n=1
	while n<=4:
		if n==1:
			string=spades
			stringSign=" of Spades"
		elif n==2:
			string=hearts
			stringSign=" of Hearts"
		elif n==3:
			string=clubs
			stringSign=" of Clubs"
		elif n==4:
			string=diamonds
			stringSign=" of Diamonds"
		i=0
		while i<len(string):
			if string[i]==1:
				name="Ace"
			elif string[i]==11:
				name="Jack"
			elif string[i]==12:
				name="Queen"
			elif string[i]==13:
				name="King"
			else:
				name=str(string[i])
			i+=1
			z+=1
			card=(name+stringSign)
			a=stringSign
			deck.append(card)
		n+=1

i=0
while i<len(deck):
	print(deck[i])
	i+=1;
k=input("Press enter to exit")