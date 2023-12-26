N=3

A=2

while(N<=200):

	if(A<N):

		if((N%A==0)):

			N+=1

			A=2

		else:

			A+=1

	else:

		print(N)

		N+=1

		A=2

print("Are the prime numbers within first 200 numbers.")

n=int(input("Number: "))

a=2

b=0

while a<n:

	if a==n-1:
		print(n," is not a prime number.")
		break
	elif n%a==0:

		print(n," is divisible by ",a)
		b=1

		a+=1
	else:

		a+=1

if b!=1:

	print(n,"is a prime number.")
k=input("Press any keys to exit")