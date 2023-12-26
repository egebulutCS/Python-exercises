name=input("What is your name?")
form=input("Would you like to use metric or imperial system?")
if form=="imperial":
	wi=float(input("How much do you weigh in pounds?"))
	hi=float(input("How tall are you in feet?"))
	weight=wi*0.454
	height=hi*0.30*100
	print(name,"your weight in metric system is",weight,"kilograms and your height is",height,"centimeters.")
elif form=="metric":
	weight=float(input("How much do you weigh in kilograms?"))
	height=float(input("How tall are you in centimeters?"))
else:
	print("You have to choose imperial or metric.")
	k=input("Press enter to exit")	
	exit()
BMI=weight/(height**2)
if(BMI<18.5):
	print(name,"you are classified as underweight.")
elif(BMI>30):
	print(name,"you are classified as obese.")
elif(BMI<29.9 and BMI>25):
	print(name,"you are classified as overweight.")
else:
	print(name,"your body mass index is just fine.")
k=input("Press enter to exit")