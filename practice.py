# Level 1
# Add up all the numbers in an array. Print out the total.

listOfNumbers = [1, 38, -28, 91, 193, 0]
sum = 0
for x in listOfNumbers:
    sum += x
print(sum)

# Level 2
# Given a list of students and a corresponding list of grades, print out the names of all students whose grade is 100.
# In this example, the program should print
# Ben
# Carl

listOfStudents = ["Abby", "Ben", "Carl", "Dave"]
listOfGrades = [95, 100, 100, 92]
name = 0
for i in range(len(listOfStudents)):
    l1 = listOfStudents
    l2 = listOfGrades
    if l2[i] == 100:
        print(listOfStudents[i])
    

# Level 3
# Print out the sum of each row in a nested (2D) list
# The output should be:
# Sum of row 1: 10
# Sum of row 2: 12
# Sum of row 3: 13

a = [ [ 2, 3, 5 ] ,
      [ 1, 4, 7 ] ,
      [ 3, 1, 9 ] ]

sum = 0
for row in a:
    for y in row:
        sum += y
    y += 1
    print(sum)
    sum = 0
   

