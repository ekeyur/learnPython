num_of_rows = int(raw_input("How many rows do you want to print? "))
for i in range(1,((num_of_rows)*2),2):
    for j in range(i,i+1):
        print " " * ((num_of_rows)-((i)/2)), "*" * j
