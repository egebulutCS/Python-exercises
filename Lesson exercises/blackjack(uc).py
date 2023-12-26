#if busted make n1 1 again and try if busts.
import math, random
n1=1
n2=2
d1=random.randint(1,13)
d2=random.randint(1,13)
if n1>10:
	if n1==11:
		string="Jack"
	elif n1==12:
		string="Queen"
	else:
		string="King"
	n1=10
	print("You drew",string)
else:
	print("You drew",n1)
if n2>10:
	if n2==11:
		string="Jack"
	elif n2==12:
		string="Queen"
	else:
		string="King"
	n2=10
	print("You drew",string)
else:
	print("You drew",n2)
if n1==1:
	n1=11
	print("You can use 1 as itself or as 11")
if n2==1:
	n2=11
	print("You can use 1 as itself or as 11")
if n1==1 and n2==1:
	n1=11
	n2=1
print("You got a total of",n1+n2)
if d1>10:
	if d1==11:
		string="Jack"
	elif d1==12:
		string="Queen"
	else:
		string=="King"
	d1=10
if d2>10:
	if d2==11:
		string="Jack"
	elif d2==12:
		string="Queen"
	else:
		string="King"
	d2=10
	print("Dealer's second card is a",string)
else:
	print("Dealer's second card is",d2)
if (n1==11 and n2==10) or (n1==10 and n2==11):
	print("ITS BLACKJACK!!!")
	m=21
	print("Dealers first card opens, its",d1)
	print("Dealer has a total of",d1+d2)
	if m<d1+d2:
		print("Dealer has a total of",d1+d2)
		print("You lose")
		k=input("Press enter to exit")
		exit()
	elif m==d1+d2:
		print("The game is a draw with",d1+d2)
		k=input("Press enter to exit")
		exit()
	elif d1+d2>m:
		print("You lose")
		k=input("Press enter to exit")
		exit()
	else:
		d3=random.randint(1,13)
		if d3>10:
			if d3==11:
				string="Jack"
			elif d3==12:
				string="Queen"
			else:
				string="King"
			d3=10
			print("Dealer drew",string)
		else:
			print("Dealer drew",d3)
		print("Dealer has a total of",d1+d2+d3)
		if d1+d2+d3>21:
			print("Dealer has busted with",d1+d2+d3)
			print("You win")
			k=input("Press enter to exit")
			exit()
		elif d1+d2+d3==m:
			print("The game is a draw with",d1+d2+d3)
			k=input("Press enter to exit")
			exit()
		elif d1+d2+d3>m:
			print("You lose")
			k=input("Press enter to exit")
			exit()
		else:
			d4=random.randint(1,13)
			if d4>10:
				if d4==11:
					string="Jack"
				elif d4==12:
					string="Queen"
				else:
					string="King"
				d4=10
				print("Dealer drew",string)
			else:
				print("Dealer drew",d4)
			print("Dealer has a total of",d1+d2+d3+d4)
			if d1+d2+d3+d4>21:
				print("Dealer has busted with",d1+d2+d3+d4)
				print("You win")
				k=input("Press enter to exit")
				exit()
			elif d1+d2+d3+d4==m:
				print("The game is a draw with",d1+d2+d3+d4)
				k=input("Press enter to exit")
				exit()
			elif d1+d2+d3+d4>m:
				print("You lose")
				k=input("Press enter to exit")
				exit()
			else:
				print("You win")
				k=input("Press enter to exit")
				exit()
if n1+n2>21:
	if n1==1:
		if 1+n2>21:
			print("Busted")
			k=input("Press enter to exit")
			exit()
	elif n2==1:
		if 1+n2>21:
			print("Busted")
			k=input("Press enter to exit")
			exit()
	else:
		pass
else:
	ans=input("Would you like to draw another card or stay?[draw/stay]")
if ans=="draw":
	n3=random.randint(1,13)
	if n3>10:
		if n3==11:
			string="Jack"
		elif n3==12:
			string="Queen"
		else:
			string="King"
		n3=10
		print("You drew",string)
	else:
		print("You drew",n3)
	print("Your total is",n1+n2+n3)
	if n1+n2+n3>21:
		if n1==1:
			if 1+n2+n3>21:
				print("Busted")
				k=input("Press enter to exit")
				exit()
		elif n2==1:
			if 1+n2^n3>21:
				print("Busted")
				k=input("Press enter to exit")
				exit()
	ans=input("Would you like to draw another card or stay?[draw/stay]")
	if ans=="draw":
		n4=random.randint(1,13)
		if n4>10:
			if n4==11:
				string="Jack"
			elif n4==12:
				string="Queen"
			else:
				string="King"
			n4=10
			print("You drew",string)
		else:
			print("You drew",n4)
		print("Your total is",n1+n2+n3+n4)
		if n1+n2+n3+n4>21:
			print("Busted with",n1+n2+n3+n4)
			k=input("Press enter to exit")
			exit()
		else:
			ans=input("Would you like to draw another card or stay?[draw/stay]")
		if ans=="draw":
			n5=random.randint(1,13)
			if n5==11:
				string="Jack"
			elif n5==12:
				string="Queen"
			else:
				string="King"
			n5=10
			print("You drew",string)
		else:
			print("You drew",n5)
		print("Your total is",n1+n2+n3+n4+n5)
		if n1+n2+n3+n4+n5>21:
			print("Busted with",n1+n2+n3+n4+n5)
			k=input("Press enter to exit")
			exit()
		elif ans=="stay":
			print("Dealers first card opens, its",d1)
			print("Dealer has a total of",d1+d2)
			if n1+n2<d1+d2:
				print("Dealer has a total of",d1+d2)
				print("You lose")
				k=input("Press enter to exit")
				exit()
			elif n1+n2==d1+d2:
				print("The game is a draw with",d1+d2)
				k=input("Press enter to exit")
				exit()
			elif d1+d2>n1+n2:
				print("You lose")
				k=input("Press enter to exit")
				exit()
			else:
				d3=random.randint(1,13)
				if d3>10:
					if d3==11:
						string="Jack"
					elif d3==12:
						string="Queen"
					else:
						string="King"
					d3=10
					print("Dealer drew",string)
				else:
					print("Dealer drew",d3)
				print("Dealer has a total of",d1+d2+d3)
				if d1+d2+d3>21:
					print("Dealer has busted with",d1+d2+d3)
					print("You win")
				elif d1+d2+d3==n1+n2:
					print("The game is a draw with",d1+d2+d3)
				elif d1+d2+d3>n1+n2:
					print("You lose")
					k=input("Press enter to exit")
					exit()
				else:
					d4=random.randint(1,13)
					if d4>10:
						if d4==11:
							string="Jack"
						elif d4==12:
							string="Queen"
						else:
							string="King"
						d4=10
						print("Dealer drew",string)
					else:
						print("Dealer drew",d4)
					print("Dealer has a total of",d1+d2+d3+d4)
					if d1+d2+d3+d4>21:
						print("Dealer has busted with",d1+d2+d3+d4)
						print("You win")
					elif d1+d2+d3+d4==n1+n2:
						print("The game is a draw with",d1+d2+d3+d4)
					elif d1+d2+d3+d4>n1+n2:
						print("You lose")
						k=input("Press enter to exit")
						exit()
					else:
						print("You win")
						k=input("Press enter to exit")
						exit()
	elif ans=="stay":
		print("Dealers first card opens, its",d1)
		print("Dealer has a total of",d1+d2)
		if n1+n2+n3<d1+d2:
			print("Dealer has a total of",d1+d2)
			print("You lose")
			exit()
		elif n1+n2+n3==d1+d2:
			print("The game is a draw with",d1+d2)
		elif d1+d2>n1+n2+n3:
			print("You lose")
			k=input("Press enter to exit")
			exit()
		else:
			d3=random.randint(1,13)
			if d3>10:
				if d3==11:
					string="Jack"
				elif d3==12:
					string="Queen"
				else:
					string="King"
				d3=10
				print("Dealer drew",string)
			else:
				print("Dealer drew",d3)
			print("Dealer has a total of",d1+d2+d3)
			if d1+d2+d3>21:
				print("Dealer has busted with",d1+d2+d3)
				print("You win")
			elif d1+d2+d3==n1+n2+n3:
				print("The game is a draw with",d1+d2+d3)
			elif d1+d2+d3>n1+n2+n3:
				print("You lose")
				k=input("Press enter to exit")
				exit()
			else:
				d4=random.randint(1,13)
				if d4>10:
					if d4==11:
						string="Jack"
					elif d4==12:
						string="Queen"
					else:
						string="King"
					d4=10
					print("Dealer drew",string)
				else:
					print("Dealer drew",d4)
				print("Dealer has a total of",d1+d2+d3+d4)
				if d1+d2+d3+d4>21:
					print("Dealer has busted with",d1+d2+d3+d4)
					print("You win")
				elif d1+d2+d3+d4==n1+n2+n3:
					print("The game is a draw with",d1+d2+d3+d4)
				elif d1+d2+d3+d4>n1+n2+n3:
					print("You lose")
					k=input("Press enter to exit")
					exit()
				else:
					print("You win")
					k=input("Press enter to exit")
					exit()
	else:
		print("Invalid choice")
elif ans=="stay":
	print("Dealers first card opens, its",d1)
	print("Dealer has a total of",d1+d2)
	if n1+n2<d1+d2:
		print("Dealer has a total of",d1+d2)
		print("You lose")
		k=input("Press enter to exit")
		exit()
	elif n1+n2==d1+d2:
		print("The game is a draw with",d1+d2)
		k=input("Press enter to exit")
		exit()
	elif d1+d2>n1+n2:
		print("You lose")
		k=input("Press enter to exit")
		exit()
	else:
		d3=random.randint(1,13)
		if d3>10:
			if d3==11:
				string="Jack"
			elif d3==12:
				string="Queen"
			else:
				string="King"
			d3=10
			print("Dealer drew",string)
		else:
			print("Dealer drew",d3)
		print("Dealer has a total of",d1+d2+d3)
		if d1+d2+d3>21:
			print("Dealer has busted with",d1+d2+d3)
			print("You win")
			k=input("Press enter to exit")
			exit()
		elif d1+d2+d3==n1+n2:
			print("The game is a draw with",d1+d2+d3)
			k=input("Press enter to exit")
			exit()
		elif d1+d2+d3>n1+n2:
			print("You lose")
			k=input("Press enter to exit")
			exit()
		else:
			d4=random.randint(1,13)
			if d4>10:
				if d4==11:
					string="Jack"
				elif d4==12:
					string="Queen"
				else:
					string="King"
				d4=10
				print("Dealer drew",string)
			else:
				print("Dealer drew",d4)
			print("Dealer has a total of",d1+d2+d3+d4)
			if d1+d2+d3+d4>21:
				print("Dealer has busted with",d1+d2+d3+d4)
				print("You win")
				k=input("Press enter to exit")
				exit()
			elif d1+d2+d3+d4==n1+n2:
				print("The game is a draw with",d1+d2+d3+d4)
				k=input("Press enter to exit")
				exit()
			elif d1+d2+d3+d4>n1+n2:
				print("You lose")
				k=input("Press enter to exit")
				exit()
			else:
				print("You win")
				k=input("Press enter to exit")
				exit()
else:
	print("Invalid input")
k=input("Press enter to exit")