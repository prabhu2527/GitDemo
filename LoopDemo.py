#for loop
obj = [2,3,5,7,9]

for i in obj:
    print(i)

for i in obj:
    print(i*2)

#sum of the first 5 Natural numbers 1+2+3+4+5 = 15
total=0
for j in range(1,6):     #iterates from 1 to 5 (6-1)\
    print(j)
    total = total + j

print(total)  #15

####################################
print("************************************************")
for k in range(1,10,2):
    print(k)        #1,3,5,7,9
print("************************************************")
for k in range(1,10,5):
    print(k)  #1,6
print("************************************************")
for k in range(10):
    print(k)  # prints 0,1,2 to 9

print("************************************************")
  #while loop
it =4
while it > 1:   #go into while loop until condition is true
    print(it)
    it -=1
print("************************************************")
  #while loop with if
it =4
while it > 1:   #go into while loop until condition is true
    if it == 3:
        pass
    else:
        print(it)       # prints 4,2
    it -=1

print("************************************************")
  #while loop with break
it =10
while it > 1:   #go into while loop until condition is true
    if it == 3:
        break
    else:
        print(it)       # prints 10 to 4
    it -=1

  #while loop with break
it =10
while it > 1:   #go into while loop until condition is true
    if it == 9:
        it -= 1
        continue  ## skip this iteration and goto next iteration
    if it == 3:
        break
    else:
        print(it)       # prints 10 to 4
    it -=1





