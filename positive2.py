nums = [8,5,-3,7,-2,12,53,-15,7,13]
new_list = []
for i in xrange(len(nums)):
    if (nums[i] > 0):
        new_list.append(nums[i])
print new_list
