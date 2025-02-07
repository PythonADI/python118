
nums = []
for i in range(1000):
    if i % 2.5 == 0:
        print(f"{i} number is divisible by 2.5")
        nums.append(i)
        continue

    print(f"{i} is not divisible by 2.5")

print(nums)

for i, num in enumerate(nums):
    if num == 10:
        print(f"We found bad number at {i} index")
        break
