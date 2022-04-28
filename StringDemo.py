str = "RahulshettyAcademy.com"
print(str[1])
print(str[0:5])  # print Rahul -substring
str1 = "consulting firm"
print(str + str1)  # concatenation
str3 = "Rahulshetty"
print(str3 in str)  # contains operation, substring check
var = str.split(".")  # splitting the string with seperator .
print(var)
print(var[0])

str4 = " great "
print(str4.strip())  # Remove spaces in both left and right
print(str4.lstrip())  # left strip remove left spaces
print(str4.rstrip())  # right strip remove right spaces
