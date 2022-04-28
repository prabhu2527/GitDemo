#with open('sample.txt','r') as file: #open is read mode
#with open('sample.txt', 'w') as file:  # open is write mode

#read the file and store it in the list
#reverse the list
#write the file

with open('sample.txt','r') as reader:
    content=reader.readlines()
    reversed(content)  #reverse the list
    with open('sample.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)   #writing line by line