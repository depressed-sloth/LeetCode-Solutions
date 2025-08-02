def twoSum(nums:list[int],target:int):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
def test():
    nums=[1,3,4,5,6,7]
    target=7
    print(twoSum(nums,target))
test()