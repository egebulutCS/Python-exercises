name=input("What is your name?")
age=int(input("How old are you?"))
form=input("Would you like to calculate in metric or imperial form?")
if form=="imperial":
	wi=float(input("How much do you weigh in pounds?"))
	hi=float(input("How tall are you in feet?"))
	weight=wi*0.454
	height=hi*0.30*100
	print(name,"you are",age,", you weigh",weight,"kilograms and your height is",height,"centimeters in the metric system.")
elif form=="metric":
	weight=float(input("How much do you weigh in kilos?"))
	height=float(input("How tall are you in meters?"))
	print(name,"you are",age,", you weigh",weight,"kilograms and your height is",height,"centimeters.")
else:
	print("Please enter metric or imperial.")
	k=input("Press enter to exit")
	exit()
gender=input("Are you male or female?")
if gender=="male":
	BMR=(10*weight)+(6.25*height)-(5*age)+5

elif gender=="female":
	BMR=(10*weight)+(6.25*height)-(5*age)-161
else:
	print("Please choose male or female.")
	k=input("Press enter to exit")
	exit()
print("The scale for exercise: \nLittle/no exercises \nlight exercise \nmoderate exercise(3-5 days/week) \nvery active(6-7 days/week) \nextra active(very active & physical job)")
exercise=input("How much do you exercise as in the scale?[little/no,light,moderate,very,extra]")
if(exercise=="little" or exercise=="no"):
	tcn=BMR*1.2
	print(name,"the total calories you need is",tcn)
elif(exercise=="light"):
	tcn=BMR*1.375
	print(name,"the total calories you need is",tcn)
elif(exercise=="moderate"):
	tcn=BMR*1.55
	print(name,"the total calories you need is",tcn)
elif(exercise=="very"):
	tcn=BMR*1.725
	print(name,"the total calories you need is",tcn)
elif(exercise=="extra"):
	tcn=BMR*1.9
	print(name,"the total calories you need is",tcn)
else:
	print("Please enter one of the values in the scale.")
print(name,"your BMR is",BMR)
k=input("Press enter to exit")