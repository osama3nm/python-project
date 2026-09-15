# Create Function 

def myhello(name = 'osama'):       # default value
    print(f"Hello {name}")

myhello("osama")                   # call function
myhello()                          # call function without argument to use default value


# Return values
def getsum(num1 , num2):
    total = num1 + num2
    return total 

print(getsum(10 ,20 ))
sum = getsum(10 , 20)
print(sum)

# Lambda function (anonymous function)
x = lambda num1 , num2 : num1 + num2 # use lambda to create a simple function
print(x(-5 , 4))

# lecture 4
a = float(input("Enter the first sum:"))
b = float(input("Enter the scond sum:"))
c = float(input("Enter the third sum:"))

