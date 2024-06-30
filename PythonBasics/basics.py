print("hello world")

a, b, c, d = 1, 2, 3.5, "Hi"
print(a, b, c, d)

# concatinating 2 diff data types
print("{} {}".format("value is", a))
print(f"the value is {c}")

#printing data types
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#list Datatye
list1 = [1, 2, 3, 5, "Sam"]
print(list1[0])
print(list1[-1])
print(list1[0:3])
list1.insert(5, "pradhan")
print(list1)
list1.append("adding at the end")
print(list1)
list1[4] = 'SAM'
print(list1)
del list1[0]
print(list1)

# Tuple DataType
Tuple1 = (1, 2, 3, 4, 5, "Samridhi")
print(Tuple1)
print(Tuple1[-1])

# Dictionary DataType
Dic1 = {"key1": "value1", "key2": 3, "key3": "Value2"}
print(Dic1)
print(Dic1["key1"])  # printed based on key and not on indexes

Dic2 = {}  #Creating dictionary
Dic2["firstname"] = "Samridhi"
Dic2["Second Name"] = "Pradhan"
Dic2["Gender"] = "Female"
print(Dic2)
print(Dic2["firstname"])

#if else loop in Python
value1 = "Hello World"
if value1 == "Hello":
    print("If loop executing")
else:
    print("value in if didn't match therefore else loop executing")
print("if else loop ended")

# for loop in Python
data1 = [1, 2, 3, 4, 5, 7]
for i in data1:
    print(i * 2)

#sum of first natural numbers:
s = 0
for i in range(1, 6):
    s = s + i
    print(s)
print(f"sum of all the number is :{s}")
print("Sum of all numbers is: {}".format(s))

print("***********")
for i in range(1, 10, 2):  #2 is for step sizing
    print(i)
print("***********")
for j in range(10):
    print(j)
print("***********")
#while loops in python
z = 6
while z > 2:
    print(z)
    z = z - 1
print("While loop ended")
print("***********")
# a = 10
# while a > 2:
#     if a != 4:
#         print(a)
#         a = a - 1
# print("***********")
a = 10
while a > 2:
    if a == 4:
        break
    print(a)
    a = a - 1
print("***********")
#continue and break : continue breaks the current iteration and goes to the next cycle(does not go to the next iteration)
c = 10
while c > 1:
    if c == 9:
        c = c-1
        continue

    if c == 4:
        break
    print(c)
    c = c - 1
print("***********")

#funtions in python

def GreetMe(name):
    print("hello,good Morning"" " + name)
# GreetMe()

GreetMe("Samridhi Pradhan ")

def AddIntegers(a,b):
    print("sum of the numbers :" ,a+b)
AddIntegers(2,3)
