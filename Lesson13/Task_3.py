

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):

    return [num ** 2 for num in nums]

def remove_negatives(nums):

    return [num for num in nums if num > 0]

def choose_func(nums, func1, func2):
    q = 0
    for i in nums:
        if i >= 0:
            q += 1
    if q == len(nums):
        return func1(nums)
    else:
        return func2(nums)


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

print(choose_func(nums1, square_nums, remove_negatives))

print(choose_func(nums2, square_nums, remove_negatives))




