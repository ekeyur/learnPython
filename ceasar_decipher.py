string = (raw_input("Enter a string to decipher from rot_13 ")).lower()

def derot13(ceasar):
    rot_13 = ''
    for i in xrange(len(ceasar)):
        if ceasar[i] == ' ':
            rot_13 += ' '
        elif (ord(ceasar[i])-13 < 97):
            rot_13 += (chr((ord(ceasar[i])-13)+97-122))
        else:
            rot_13 += (chr(ord(ceasar[i])-13))
    print ''.join(rot_13)

derot13(string)
