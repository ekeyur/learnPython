text = (raw_input("Enter a string to convert to rot_13: ")).lower()

def rot13(text):
    ceasar = text.lower() # Converting the text into lowercase
    rot_13 = '' # Defining an empty string
    for i in xrange(len(ceasar)): # looping through the whole string
        if ceasar[i] == ' ': # if the string has space
            rot_13 += ' ' # Adding a space in the next line

        #if the value exceeds 122(ASCII value of 'z') after adding 13 to each assci value
        elif (ord(ceasar[i])+13 > 122):
            #Adding the spillover chars to 96 to get the right rot13 value
            rot_13 += (chr((ord(ceasar[i])+13) - 122 + 96)) #

        else:
        #just adding the 13 offset ASCII char to string
            rot_13 += (chr(ord(ceasar[i])+13))
    return ''.join(rot_13) # Converting the list of chars to string and returning it.

print rot13(text)
