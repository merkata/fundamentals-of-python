# Get two numbers from the user
n1 = float(input())
n2 = float(input())
# Compute sum of the two numbers
print("'n1 + n2' is correct");
print(n1 + n2)
# Compute average of the two numbers
print("'n1+n2/2' is locical error. Have to be '(n1+n2)/2'")
print( (n1 + n2)/2 )
# Assign some variables
print("assignment 'd1 = d2 = 0' is correct")
d1 = d2 = 0
# Compute a quotient
print("'n1/d1' is division by zero error. Could be 'd1/n1'")
print(d1/n1)
# Compute a product
print("'n1*n2 = d1' is incorrect. Have to be 'd1 = n1*n2'")
d1 = n1*n2
# Print result
print(d1)

