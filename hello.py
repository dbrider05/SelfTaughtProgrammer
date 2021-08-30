num = input("Enter an Integer:")
try:
	num = int(num)
	print(num)
except ValueError:
	print("Please type an integer")