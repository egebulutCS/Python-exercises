import math, random, time
p1=random.randint(1,13)
p2=random.randint(1,13)
d1=random.randint(1,13)
d2=random.randint(1,13)
totala=None
# p1 draw
if p1>10 and p1!=1:
	if p1==11:
		string="Jack"
	elif p1==12:
		string="Queen"
	else:
		string="King"
	p1=10
	print("You drew a",string)
else:
	print("You drew",p1)
time.sleep(0.5)
# p2 draw
if p2>10 and p2!=1:
	if p2==11:
		string="Jack"
	elif p2==12:
		string="Queen"
	else:
		string="King"
	p2=10
	print("You drew a",string)
else:
	print("You drew",p2)
time.sleep(0.5)
# p1 ace
if p1==1:
	totala=p2+11
	print("You drew an Ace")
# p2 ace
if p2==1:
	totala=p1+11
	print("You drew an Ace")
# both p1 and p2 ace
if p1==1 and p2==1:
	totala=12
	print("You drew double Ace")
total=p1+p2
if totala==None:
	print("You got a total of",total)
else:
	print("You got a total of",total,"or",totala)
time.sleep(0.5)
# d2 draw
print("Dealer's first card is not revealed.")
if d2>10:
	if d1==11:
		string="Jack"
	elif d1==12:
		string ="Queen"
	else:
		string="King"
	d2=10
	print("Dealer's second card is a",string)
else:
	print("Dealer's second card is",d2)
time.sleep(0.5)
# blackjack condition
if (p1==1 and p2==10) or (p1==10 and p2==1):
	print("ITS BLACKJACK!!!")
	print("You win")
	k=input("Press enter to exit")
	exit()
# draw decision
ans=input("Would you like to draw another card or stay?[d/s]")
while ans=="d":
	# p3 draw
	p3=random.randint(1,13)
	if p3>10:
		if p3==11:
			string="Jack"
		elif p3==12:
			string="Queen"
		else:
			string="King"
		p3=10
		print("You drew",string)
	else:
		print("You drew",p3)
	time.sleep(0.5)
	if (total<=11 and p3==1):
		totala=total+11
	else:
		totala=None
	total+=p3
	if (totala==None):
		print("Your total is",total)
	else:
		print("Your total is",total,"or",totala)
	time.sleep(0.5)
	# bust check
	if total>21:
		print("Busted")
		k=input("Press enter to exit")
		exit()
	else:
		ans=input("Would you like to draw another card or stay?[d/s]")
# stay
if ans=="s":
	if (totala!=None):
		if (totala<=21):
			total=totala
	# d1 reveal
	if d1>10:
		if d1==11:
			string="Jack"
		elif d1==12:
			string="Queen"
		else:
			string="King"
		d1=10
		print("Dealer's first card is revealed, it is a",string)
	else:
		print("Dealer's first card is revealed, it is",d1)
	time.sleep(0.5)
	totald=d1+d2
	print("Dealer has a total of",totald)
	# d3 draw	
	while (totald<total):
		d3=random.randint(1,13)
		if d3>10:
			if d3==11:
				string="Jack"
			elif d3==12:
				string="Queen"
			else:
				string="King"
			d3=10
			print("Dealer's next card is a",string)
		else:
			print("Dealer's next card is",d3)
		time.sleep(0.5)
		totald+=d3
		print("Dealer has a total of",totald)
		time.sleep(0.5)
		# bust check
		if totald>21:
			print("Dealer busted")
			print("You win")
			k=input("Press enter to exit")
			exit()
	# draw game
	if totald==total:
		print("It is a draw")
		k=input("Press enter to exit")
		exit()
	else:
		print("Dealer wins")
	
k=input("Press enter to exit")