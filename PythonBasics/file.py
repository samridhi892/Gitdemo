file = open('text.txt')

# print(file.read())  # prints all the contents in a file
# print(file.read(3))  # prints only first 3 character in a file

# print(file.readline())  # this will read the lines in a file
# print(file.readline())

# line = file.readline()    # read all the contents in the file  using while loop
# while line != "":
#     print(line)
#     line = file.readline()

for i in file.readlines():  #  read all contents in the file using for loop
    print(i)

file.close()
