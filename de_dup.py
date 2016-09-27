list = [4,9,5,6,1,5,2,2]

def remove_dup(rem):
    temp_list = []
    for i in list:
        if i not in temp_list:
            temp_list.append(i)
    print temp_list

remove_dup(list)
