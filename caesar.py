def makeCipher(message, offset):
    new_char = ("")
    # chars = message.split()
    # for word in chars:
    for char in message:
        num = ord(char)
        num = (num + offset) % 128
        new_char += chr(num)
    #num = ord(string)
    #num = (num + offset) % 128
    #new_ch = chr(num)    
    return new_char

message = str(input("Enter a string to be turned into a cipher: "))
offset = int(input("Enter an offset for your cipher: "))
cipher = makeCipher(message, offset)
print("You're new cipher is: {}".format(cipher))

print("Decoded it is:", makeCipher(cipher, offset*-1))