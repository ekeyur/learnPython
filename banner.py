banner = raw_input("Please enter a string: ")
for i in range(1,4):
        if i%2 != 0:
            print "*" * ((len(banner))+6)
        else:
            print "* ",banner," *"
