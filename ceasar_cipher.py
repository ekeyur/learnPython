ceasar = raw_input("Enter a string to reverse: ")
rot_13 = []
# Converting the string to rot_13
for i in xrange(0,len(ceasar)-1):
    rot_13[i] = ord(ceasar[i]) + 13

# Printing the rot_13 string
for i in rot_13:
    print i
