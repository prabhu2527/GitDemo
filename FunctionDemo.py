# in python, function is group of related statements that perform a specific task

# Function definition
def GreetMe():
    print("Good Morning")


# Function call
GreetMe()  # invoking a function or call a function


# parameterized Function definition
def GreetMe(name):
    print("Good Morning " + name)


# Function call
GreetMe("prabhu")  # invoking a function or call a function


##################################
def AddInteger(a, b):
    print(a + b)


AddInteger(4, 3)  # 7


###############################
def AddInteger(a, b):
    return (a + b)


print(AddInteger(4, 3))  # 7
