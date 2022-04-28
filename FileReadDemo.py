file= open('sample.txt')
#print(file.read()) #read all the contents of the file

#print(file.read(2)) #read first 2 letters of file

#print(file.read(5)) #read first 5 letters of file
#print(file.readline()) #reads the first line. reads a single line at time
#print(file.readline()) #reads next line


##print line by line using readline method
# line=file.readline()
# while (line != ""):
#     print(line)
#     line = file.readline()

#reads all lines and stores in list
# val = file.readlines()
# print(val)

for line in file.readlines():
    print(line)
file.close()