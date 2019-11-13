#Strings and variables
from django.template.defaultfilters import upper, lower
DOB = 1992 #the year you are born
AGE = 2019 - DOB
am = "Your age is {}, and you are born in {}.".format(AGE, DOB)
print(am)
str="Your name is {}.".format("Raj")
print(str)
str2="Your age is {}.".format(22)
print(str2)
yolo = upper("tanpis")
print(yolo)