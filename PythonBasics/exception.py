x = 2
if x!=0:
    # raise Exception("Error occured")
    pass

assert (x==2)

try:
    with open("file1.txt","r") as write:
        write.read()
except Exception as e:
    print(e)
finally :
    print("executing finally always")
