import math, random, time
p1=random.randint(1,13)
p2=random.randint(1,13)
d1=random.randint(1,13)
d2=random.randint(1,13)
totala=None
h1=None
h2=None
total1=None
total2=None
totala1=None
totala2=None
c=None
d=None
e=0
f=2
g=0
l=0
# p1 draw
if p1>10 and p1!=1:
	if p1==11:
		string="Jack"
		c=1
	elif p1==12:
		string="Queen"
		c=2
	else:
		string="King"
		c=3
	p1=10
	print("You drew a",string)
else:
	print("You drew",p1)
time.sleep(0.5)
# p2 draw
if p2>10 and p2!=1:
	if p2==11:
		string="Jack"
		d=1
	elif p2==12:
		string="Queen"
		d=2
	else:
		string="King"
		d=3
	p2=10
	print("You drew a",string)
else:
	print("You drew",p2)
time.sleep(0.5)
# split
if (p1==p2) and (c==d):
	spl=input("Do you want to split?[Y/N]")
	if (spl=="y") or (spl=="Y"):
		h1=random.randint(1,13)
		h2=random.randint(1,13)
		# h1 draw
		if h1>10 and h1!=1:
			if h1==11:
				string="Jack"
			elif h1==12:
				string="Queen"
			else:
				string="King"
			h1=10
			print("You drew a",string,"for the first pair")
		else:
			print("You drew",h1,"for the first pair")
		time.sleep(0.5)
		# h2 draw
		if h2>10 and h2!=1:
			if h2==11:
				string="Jack"
			elif h2==12:
				string="Queen"
			else:
				string="King"
			h2=10
			print("You drew a",string,"for the second pair")
		else:
			print("You drew",h2,"for the second pair")
		time.sleep(0.5)
		# h1 ace
		if h1==1 and p1!=1:
			totala1=p1+11
			print("You drew an Ace for the first pair")
		# h2 ace
		if h2==1 and p2!=1:
			totala2=p2+11
			print("You drew an Ace for the second pair")
if h1==None:
	# p1 ace
	if p1==1:
		totala=p2+11
	# p2 ace
	if p2==1:
		totala=p1+11
	total=p1+p2
	if totala==None:
		print("You got a total of",total)
	else:
		print("You got a total of",total,"or",totala)
	time.sleep(0.5)
else:
	# p1 ace with h1
	if p1==1 and h1!=1:
		totala1=h1+11
	# p2 ace with h2
	if p2==1 and h2!=1:
		totala2=h2+11
	time.sleep(0.5)
	total1=p1+h1
	total2=p2+h2
	if totala1==None:
		print("First pair's total is",total1)
	else:
		print("First pair's total is",total1,"or",totala1)
	if totala2==None:
		print("Second pair's total is",total2)
	else:
		print("Second pair's total is",total2,"or",totala2)
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
if h1!=None:
	if (p1==1 and p2==10) or (p1==10 and p2==1):
		print("ITS BLACKJACK!!!")
		print("You win")
		k=input("Press enter to exit")
		exit()
# blackjack for pairs
if (p1==1 and h1==10) or (p1==10 and h1==1):
	print("FIRST PAIR IS BLACKJACK!!!")
	print("You win with the first pair")
	e=1
if (p2==1 and h2==10) or (p2==10 and h2==1):
	print("SECOND PAIR IS BLACKJACK!!!")
	print("You win with the second pair")
	f=1
if e==f:
	print("You win with double blackjack")
	k=input("Press enter to exit")
	exit()
# draw decision wo/pairs
if h1==None:
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
	# stay wo/pairs
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
		# draw game wo/pairs
		if totald==total:
			print("It is a draw")
			k=input("Press enter to exit")
			exit()
		else:
			print("Dealer wins")
else:
	# draw decision w/pairs
	if e==0:
		ans1=input("Would you like to draw another card for the first pair or stay?[d/s]")
	elif e==1:
		ans1="s"
	while ans1=="d":
		# h3 draw
		h3=random.randint(1,13)
		if h3>10:
			if h3==11:
				string=("Jack")
			elif h3==12:
				string=("Queen")
			else:
				string=("King")
			h3=10
			print("You drew a",string,"for the first pair")
		else:
			print("You drew",h3,"for the first pair")
		time.sleep(0.5)
		if (total1<=11 and h3==1):
			totala1=total1+11
		else:
			totala1=None
		total1+=h3
		if (totala1==None):
			print("Your total for first pair is",total1)
		else:
			print("Your total for first pair is",total1,"or",totala1)
		time.sleep(0.5)
		# bust check for pair 1
		if total1>21:
			print("First pair busted")
			g=1
			ans1="s"
		else:
			ans1=input("Would you like to draw another card for the first pair or stay?[d/s]")
	if f==2:
		ans2=input("Would you like to draw another card for the second pair or stay?[d/s]")	
	elif f==1:
		ans2="s"
	while ans2=="d" and ans1=="s":	
		# h4 draw
		h4=random.randint(1,13)
		if h4>10:
			if h4==11:
				string=("Jack")
			elif h4==12:
				string=("Queen")
			else:
				string=("King")
			h4=10
			print("You drew a",string,"for the second pair")
		else:
			print("You drew",h4,"for the second pair")
		time.sleep(0.5)
		if (total2<=11 and h4==1):
			totala2=total2+11
		else:
			totala2=None
		total2+=h4
		if (totala2==None):
			print("Your total for second pair is",total2)
		else:
			print("Your total for second pair is",total2,"or",totala2)
		time.sleep(0.5)
		# bust check for pair 2
		if total2>21:
			if g==1:
				print("Second pair busted as well")
				k=input("Press enter to exit")
				exit()
			else:
				print("Second pair busted")
				l=1
				ans2="s"
		else:
			ans2=input("Would you like to draw another card for the second pair or stay?[d/s]")
	# stay w/pairs
	if ans2=="s" or ans1=="s":
		if(totala1!=None):
			if(totala1<=21):
				total1=totala1
		if (totala2!=None):
			if(totala2<=21):
				total2=totala2
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
		while (totald<total1) and (totald<total2):
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
			# bust check w/ pairs
			if totald>21:
				print("Dealer busted")
				if (g!=1 or f==1) and (l!=1 or e==1):
					print("You win with both of the pairs")
				elif g!=1 or f==1:
					print("You win with the second pair")
				elif l!=1 or e==1:
					print("You win with the first pair")
				k=input("Press enter to exit")
				exit()
		# draw game w/ pairs
		if (totald==total1) and (totald==total2):
			print("Both paira are draw")
			k=input("Press enter to exit")
			exit()
		elif (totald==total1) and (e==0):
			print("First pair is a draw")
			if (totald<total2):
				print("You win with the second pair")
			elif (totald>total2):
				print("You lose with the second pair")
			k=input("Press enter to exit")
			exit()
		elif (totald==total2) and (f==0):
			print("Second pair is a draw")
			if (totald<total1):
				print("You win with the second pair")
			elif (totald>total1):
				print("You lose with the second pair")
			k=input("Press enter to exit")
			exit()
		elif (totald>total1) and (totald<total2):
			print("Dealer wins against first pair but loses to the second")
			k=input("Press enter to exit")
			exit()
		elif (totald<total1) and (totald>total2):
			print("Dealer wins against second pair bur loses to the first")
			k=input("Press enter to exit")
			exit()
		else:
			print("Dealer wins against both pairs")
			
k=input("Press enter to exit")