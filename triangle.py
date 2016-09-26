height = int(raw_input("How many rows do you want to print? "))

for row_num in range(height):
    base_width = (2 * height) - 1
    num_of_stars = (row_num * 2) + 1
    num_of_spaces = (base_width - num_of_stars)/2

    stars = "*" * num_of_stars
    spaces = " " * num_of_spaces
    print "%s%s" % (spaces,stars)
