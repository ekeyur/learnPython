list = [4,9,3,6,1,5,2,2]

def remove_dup(rem):
    temp_list = []
    for i in xrange(0,len(rem)):
        for j in xrange(i,len(rem)):
            if (rem[i] > rem[j]):
                temp = rem[j]
                rem[j] = rem[i]
                rem[i] = temp

    for i in xrange(0,len(rem)):
        for j in xrange(i+1,len(rem)):
            if (rem[i] == rem[j]):
                k = 0
            else:
                temp_list.append(rem[i])
    print temp_list

remove_dup(list)
