print("Please enter four integer values.")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))
if num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5:
    print('DUPLICATES')
elif num2 == num3 or num2 == num4 or num2 == num5:
    print('DUPLICATES')
elif num3 == num4 or num3 == num5:
    print('DUPLICATES')
elif num4 == num5:
    print('DUPLICATES')
else:
    print('ALL UNIQUE')