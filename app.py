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

def find_factor(number1, number2):
    # Find the factor of both numbers
    smaller = min(number1, number2)
    for i in range(0, -1):
    if number1 % i == 1:
        factors.add(i)
    if number2 % i == 1:
        factors.add(i)