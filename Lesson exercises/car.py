print("Numbers for cars:\nFord=1\nBMW=2\nMercedes=3\nLamborghini=4\nFerrari=5\nBugatti=6")
while True:
	car=int(input("Which car do you want?"))
	if car==1:
		car1="Ford"
		print("You have chosen",car1)
		price=10000
		break
	elif car==2:
		car1="BMW"
		print("You have chosen",car1)
		price=20000
		break
	elif car==3:
		car1="Mercedes"
		print("You have chosen",car1)
		price=30000
		break
	elif car==4:
		car1="Lamborghini"
		print("You have chosen",car1)
		price=40000
		break
	elif car==5:
		car1="Ferrari"
		print("You have chosen",car1)
		price=50000
		break
	elif car==6:
		car1="Bugatti"
		print("You have chosen",car1)
		price=60000
		break
	else:
		print("Please choose a valid option.") 
while True:
	ac=input("Do you want air conditioner for £1000?[Y/N]")
	if ac=="y" or ac=="Y":
		acprice=1000
		break
	elif ac=="n" or ac=="N":
		acprice=0
		break
	else:
		print("Please choose a valid option.")
while True:
	ww=input("Do you want wide wheels for £500?[Y/N]")
	if ww=="y" or ww=="Y":
		wwprice=500
		break
	elif ww=="n" or ww=="N":
		wwprice=0
		break
	else:
		print("Please choose a valid option.")
while True:
	mc=input("Do you want metalic paint for £750?[Y/N]")
	if mc=="y" or mc=="Y":
		mcprice=750
		break
	elif mc=="n" or mc=="N":
		mcprice=0
		break
	else:
		print("Please choose a valid option.")
while True:
	if car1=="Ford":
		print("Sunroof is not available for Ford.")
		srprice=0
		break
	sr=input("Do you want sunroof for £800?[Y/N]")
	if sr=="y" or sr=="Y":
		srprice=800
		break
	elif sr=="n" or sr=="N":
		srprice=0
		break
	else:
		print("Please choose a valid option.")
print("You have chosen",car1)
print("Air conditioner:",acprice)
print("Wide Wheels:",wwprice)
print("Metalic Paint:",mcprice)
print("Sunroof:",srprice)
totalPrice=str(price+acprice+wwprice+mcprice+srprice)
print("Total price of the car is £"+totalPrice)
k=input("Press enter to exit")
