"""  x = 3
y = float(3)
print(x,y) """

"""  values = []
print(This is a thing)
for i in values:
    print(i) """

""" print(values[0])
print(values[6])  """

""" "This is a thing"
x = "This is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """

""" service = input("Was the service bad, okay, good, or great? ")
if service == "bad":
    print("You tipped 0%")
elif service == "okay":
    print("You tipped 15%")
elif service == "good":
    print("You tipped 20%")
elif service == "great":
    print("You tipped 25%") """

# Python Program to find the factors of a number

# This function computes the factor of the argument passed
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 60

print_factors(num)


# Python Program to find the factors of a number

# This function computes the factor of the argument passed
def print_factors(y):
   print("The factors of",y,"are:")
   for i in range(1, y + 1):
       if y % i == 0:
           print(i)

num = 120

print_factors(num)

#find the gcf of x and y
def gcf(x,y):
    if x == 60 and y == 120:
        print('Find the gcf of x and y')
        