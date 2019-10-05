#i = "no"
#while i == "no":
   #i = input("Do you want ice cream? ")

#a = 0
#number = int(input("Input any number "))
#while a < number:
    #print(a)
    #a += 2

number = int(input("Input any positive number "))
x = 2
is_prime = True
while x < number:
    y = 2
    while y < x:
        if x % y == 0:
            is_prime = False
            break
        else:
            is_prime = True
        y += 1
    if is_prime == True:
        print(x)
    x += 1

