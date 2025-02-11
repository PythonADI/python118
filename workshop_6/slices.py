nums = [1, 2, 3, 4, 5]
# x = [1, 2, 3, 4, 5]
# x = nums[:]
# x = nums.copy()
x = nums[:3]

print(f'{x == nums = }')
# print(f'{id(x) == id(nums) = }')
print(f'{x is nums = }')

print(f'{id(nums) = }')
print(f'{id(x) = }')
print(f'{x = }')

x[0] = 5
print(f'{nums = }')
print(f'{x = }')