triangle = int(raw_input("Enter a number between 1 and 100: "))
print "The first %d triangle numbers are: "
for n in range(1,triangle+1):   
    print "%d : %d" % (n,n*(n+1)/2)
