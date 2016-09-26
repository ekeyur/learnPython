nums = [2,5,3,7,12,53,5,7,13]

for i in xrange(0,len(nums)):
    for j in xrange(i,len(nums)):
        if(nums[i] > nums[j]):
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
print nums[len(nums)-1]
