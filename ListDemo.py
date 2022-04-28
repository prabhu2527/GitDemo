values = [1,2,"rahul",4.5,7]
#list is data type allows multiple values and can be of different data types
print(values[0]) # 1
print(values[3]) #4.5

print(values[-1]) #7
print(values[1:3]) #2,"rahul"
values.insert(3,"shetty")  #insert value at position 3
print (values)
values.append("End") #add value at the end of the list [1,2,"rahul","shetty",4.5,7,"End"]
print(values)
values[2]="RAHUL" #updating
del values[0]
print(values)  #[1, 2, 'rahul', 'shetty', 4.5, 7, 'End']

values.remove("End") #removes the given value from the list
print(values) #[2, 'RAHUL', 'shetty', 4.5, 7]
values.reverse() #reverse the list
print(values)  #[7, 4.5, 'shetty', 'RAHUL', 2]
values.pop(0) #removes value at the given index
print (values) #[4.5, 'shetty', 'RAHUL', 2]
values.pop(2)
print(values) #[4.5, 'shetty', 2]
values.count(2) #counts the given value in the list
print(values.count(2)) #1
value1=values.copy() #return shallow copy of the list
print(value1) #[4.5, 'shetty', 2]
values.extend([2,4,5])  ##extend the list by appending from the list or iterable
print(values)  #[4.5, 'shetty', 2, 2, 4, 5]
values.extend((3,4,5))
print(values) #[4.5, 'shetty', 2, 2, 4, 5, 3, 4, 5]
values.extend({1,2})
print(values)  #[4.5, 'shetty', 2, 2, 4, 5, 3, 4, 5, 1, 2]
values.clear()  #removes all the elements from the list
print(values)  #[]

