# import random

nums = []

for i in range(100):
    nums.append(i)

# random.shuffle(nums)

print(len(nums))
print(nums[:10])
# for i, num in enumerate(nums):
#     if i > 9:
#         break

#     print(num)
print(nums)
print(nums[-10:])
for _ in range(10):
    nums.pop()
print(nums[-10:])

print(nums)
# nums[5] = 8
# print(nums[5])
# print(nums[:10])

for i, num in enumerate(nums):
    if i % 2 == 1:
        nums[i] **= 2

print(nums)
