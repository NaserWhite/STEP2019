print("A. Text to Morse Code")
print("B. Text to Binary Code")
option = input("Select an option ")

while option != "A" and option != "B":
    print("A. Text to Morse Code")
    print("B. Text to Binary Code")
    option = input("Select an option ")
    


if option == "A":
    text = input("Enter Text ")
    for x in text:
        if x == "A" or x == "a":
            print(".-", end = "")
        if x == "B" or x == "b":
            print("-...", end = "")
        if x == "C" or x == "c":
            print("-.-.", end = "")
        if x == "D" or x == "d":
            print("-..", end = "")
        if x == "E" or x == "e":
            print(".", end = "")
        if x == "F" or x == "f":
            print("..-.", end = "")
        if x == "G" or x == "g":
            print("--.", end = "")
        if x == 'H' or x == 'h':
            print("....", end = "")
        if x == "I" or x == "i":
            print("..", end = "")
        if x == "J" or x == "j":
            print(".---", end = "")
        if x == "K" or x == "k":
            print("-.-", end = "")
        if x == "L" or x == "l":
            print(".-..", end = "")
        if x == "M" or x == "m":
            print("--", end = "")
        if x == "N" or x == "n":
            print("-.", end = "")
        if x == "O" or x == "o":
            print("---", end = "")
        if x == "P" or x == "p":
            print(".--.", end = "")
        if x == "Q" or x == "q":
            print("--.-", end = "")
        if x == "R" or x == "r":
            print(".-.", end = "")
        if x == "S" or x == "s":
            print("...", end = "")
        if x == "T" or x == "t":
            print("-", end = "")
        if x == "U" or x == "u":
            print("..-", end = "")
        if x == "V" or x == "v":
            print("...-", end = "")
        if x == "W" or x == "w":
            print(".--", end = "")
        if x == "X" or x == "x":
            print("-..-", end = "")
        if x == "Y" or x == "y":
            print("-.--", end = "")
        if x == "Z" or x == "z":
            print("--..", end = "") 
        if x == " ":
            print("/,", end = "")
        if x == "0":
            print("-----", end = "")
        if x == "1":
            print(".----", end = "")
        if x == "2":
            print("..---", end = "")
        if x == "3":
            print("...--", end = "")
        if x == "4":
            print("....-", end = "")
        if x == "5":
            print(".....", end = "")
        if x == "6":
            print("-....", end = "")
        if x == "7":
            print("--...", end = "")
        if x == "8":
            print("---..", end = "")
        if x == "9":
            print("----.", end = "")


if option == "B":
    text = input("Enter Text ")
    for x in text:
        if x == "A":
            print("01000001", end = "")
        if x == "a":
            print("01100001", end = "")
        if x == "B":
            print("01000010", end = "")
        if x == "b":
            print("01100010", end = "")
        if x == "C":
            print("01000011", end = "")
        if x == "c":
            print("01100011", end = "")
        if x == "D":
            print("01000100", end = "")
        if x == "d":
            print("01100100", end = "")
        if x == "E":
            print("01000101", end = "")
        if x == "e":
            print("01100101", end = "")
        if x == "F":
            print("01000110", end = "")
        if x == "f":
            print("01100110", end = "")
        if x == "G":
            print("01000111", end = "")
        if x == "g":
            print("01100111", end = "")
        if x == "H":
            print("01001000", end = "")
        if x == "h":
            print("01101000", end = "")
        if x == "I":
            print("01001001", end = "")
        if x == "i":
            print("01101001", end = "")
        if x == "J":
            print("01001010", end = "")
        if x == "j":
            print("01101010", end = "")
        if x == "K":
            print("01001011", end = "")
        if x == "k":
            print("01101011", end = "")
        if x == "L":
            print("01001100", end = "")
        if x == "l":
            print("01101100", end = "")
        if x == "M":
            print("01001101", end = "")
        if x == "m":
            print("01101101", end = "")
        if x == "N":
            print("01001110", end = "")
        if x == "n":
            print("01101110", end = "")
        if x == "O":
            print("01001111", end = "")
        if x == "o":
            print("01101111", end = "")
        if x == "P":
            print("01010000", end = "")
        if x == "p":
            print("01110000", end = "")
        if x == "Q":
            print("01010001", end = "")
        if x == "q":
            print("01110001", end = "")
        if x == "R":
            print("01010010", end = "")
        if x == "r":
            print("01110010", end = "")
        if x == "S":
            print("01010011", end = "")
        if x == "s":
            print("01110011", end = "")
        if x == "T":
            print("01010100", end = "")
        if x == "t":
            print("01110100", end = "")
        if x == "U":
            print("01010101", end = "")
        if x == "u":
            print("01110101", end = "")
        if x == "V":
            print("01010110", end = "")
        if x == "v":
            print("01110110", end = "")
        if x == "W":
            print("01010111", end = "")
        if x == "w":
            print("01110111", end = "")
        if x == "X":
            print("01011000", end = "")
        if x == "x":
            print("01111000", end = "")
        if x == "Y":
            print("01011001", end = "")
        if x == "y":
            print("01111001", end = "")
        if x == "Z":
            print("01011010", end = "")
        if x == "z":
            print("01111010", end = "")
        if x == " ":
            print("00100000", end = "")
        if x == ".":
            print("101110", end = "")
