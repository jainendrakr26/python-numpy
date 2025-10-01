def twoSum(nums, target):
    n=len(nums)
    for i in range(n):
        for j in range(i+i):
            if nums[i]+nums[j]==target:
                return [i,j]
nums=[1,2,4,6,8,11]
target=14
print(twoSum(nums,target))