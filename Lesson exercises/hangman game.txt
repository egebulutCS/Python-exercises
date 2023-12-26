word=input("Enter the key word:")
guess=""
used=""
i=0
while i<len(word):
	guess+="_"
	i+=1
lives=10
while lives!=0:
	print("You have",lives,"lives left.")
	ans=input("Do you want to guess the word?[Y/N]")
	if ans=="y" or ans=="Y":
		letter=input("Guess the word:")
		if letter==word:
			print("Congragulations you win!!!")
			print("The word was",word)
			k=input("Press enter to exit")
			exit()
		else:
			lives-=1
			print("Your guess was wrong.")
	if ans=="n" or ans=="N":
		b=0
		if len(used)!=0:
			print("You have used letters",used)
		n=0
		letter=input("Guess a letter:")
		while len(letter)!=1:
			letter=input("Please enter a letter:")
		while n<len(used):
			if letter==used[n]:
				print("You have used",letter,"before.")
				letter=input("Please enter a new letter:")
			else:
				n+=1
		used+=letter
		used+=" "
		index=0
		while index<len(word):
			if letter==word[index]:
				guess=guess[0:index]+letter+guess[index+1:]
				b=1
			index+=1
		if b==0:
			lives-=1
		print(guess)
		if guess==word:
			print("Congragulations you win!!!")
			print("The word was",word)
			k=input("Press enter to exit")
			exit()
print("You have ran out of lives.")
k=input("Press enter to exit")