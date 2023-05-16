nums = [4,5,6,3]
target = 9
l = len(nums)
num_indices = {}

for index in range(l):
    num = nums[index]
    complement = target - num
    if complement in num_indices:
        return [num_indices[complement], index]
    num_indices[num] = i
