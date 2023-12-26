import math, random
q="y"

while q=="Y" or q=="y":
	
	two=[]
	counter=0
	while counter<2:
		dice = random.randint(1,6)

		print("You rolled a ",dice)

		two.append(dice)
		counter+=1
	print(two)
	q=input("Do you want to roll the dice again?[Y/N]")
k=input("Press enter to exit")