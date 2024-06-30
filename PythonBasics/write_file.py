#Reverse the data in the file and update the file

#read the files and store all the lines in a list
#reverse the list
#write the list back into the file

with open("text.txt", "r") as file_read:
    contents = file_read.readlines()  #[Hello How Are You doing]
    reversed(contents) #[doing You Are How Hello]
    with open('text.txt', 'w') as file_write:

        for line in reversed(contents):
            file_write.write(line)
