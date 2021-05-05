def sum(nums, target):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            num1 = nums[x]
            num2 = nums[y]
            final = num1 + num2
            if(final == target):
                return [x, y]

print(sum([2,7,11,15],9)) 