# 1. Write down what you think the output of these statements
#       will be BEFORE you run the code.
'''
print("Hello world")
print("I am", 13)
print("I can co" + "de")
print("There are", 6, "apples " + "on the tree")

# 2. Modify the second print statement so you get the same output
#       without using commas.

cityName = input("Enter a city name: ")
print("It was a dark and stormy night in " +  cityName + ". [Rest of background here]")
'''

#fav_color = input("What is your favorite color? ")
#print("Your Favorite color is " + fav_color)
'''
age = input("What is your age? ")
age = int(age)
older = age + 70

print ("In five years, you will be " + str(older))
'''

age= input("How old are you? ")
age = int(age)
year = input("What Year is it? ")
year = int(year)
time = input("How many years do you want to skip? ")
time = int(time)

older = age + time
newyear = year + time

print("In " + str(time) + " years you will be " + str(older) + " years old. And the year will be " + str(newyear))