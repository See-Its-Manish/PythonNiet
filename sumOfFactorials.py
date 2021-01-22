# Print the sum of the series: 1! + 2! + 3! + ------ + n!

n=int(input("Enter a number: "))

sumOfSeries=0
while(n!=0):
	product = 1;
	for i in range(1,n+1):
		product*=i
	sumOfSeries+=product
	n-=1

print("Sum of the series: ", sumOfSeries)