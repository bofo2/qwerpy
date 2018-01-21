print("Hello I'm gonna try some crazy shit you ready for this")
input("press enter")

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return (fib(n - 1) + fib(n - 2))

choice = int(input("How deep into fibo? "))

fibo = range(0, choice)

for element in fibo:
	print(fib(element))


