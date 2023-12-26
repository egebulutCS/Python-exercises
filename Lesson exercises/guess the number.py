import math, random
number=random.randint(1,100)
guess=int(input("What is the number I am thinking between 1 and 100?"))
counter=1
while guess!=number:
	if guess<number:
		print("The number is higher than your guess.")
		guess=int(input("Your next guess:"))
		counter+=1
	if guess>number:
		print("The number is lower than your guess.")
		guess=int(input("Your next guess:"))
		counter+=1
print("Congragulations you found the number in",counter,"tries, it was",number,"!!!")
k=input("Press enter to exit")