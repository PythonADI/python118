def find(search_list, search_element):
    for i, element in enumerate(search_list):
        if search_element == element:
            return i

    return -1

nums = [1, 2, 3, 4, 5]
idx = find([1, 2, 3, 5], 7)
print(f"{idx = }")

idx = find(nums, 5)
print(f"{idx = }")

idx = find(nums, -5)
print(f"{idx = }")


print(f"{find([1, 2, 3], nums) = }")

# grid = [
#     [1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 1],
#     [1, 1, 1, 0, 1],
#     [1, 0, 0, 0, 1],
#     [1, 1, 0, 1, 1],
#     [1, 0, 0, 1, 1],
#     [1, 0, 1, 1, 1],
# ]
# print(grid[5][2])
