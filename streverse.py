rev = raw_input("Enter a string to reverse: ")
for i in xrange(len(rev)-1,-1,-1):
    print ''.join(rev[i])
