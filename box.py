height = int(raw_input("height? "))
width = int(raw_input("width? "))

for i in range (0,height):
    if i%2 != 0:
        if i == 1 or i == height-1:
            print "*" * width
        else:
            print "*", " " * (width - 4),"*"
