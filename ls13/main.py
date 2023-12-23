# 3! => 1 * 2 * 3 = 6

# def factorial(n):
#     result = 1
#     while n != 1:
#         result *= n
#         n -= 1
#     return result

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1

#     return factorial(n-1) * n


# print(factorial(3))
# print(factorial(4))


# import os


# def list_files(dir):
#     for filename in os.listdir(dir):
#         path = os.path.join(dir, filename)

#         if os.path.isdir(path):
#             list_files(path)
#         else:
#             print(path)


# list_files('.')

# Quicksort
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[len(arr) // 2]
#         left, middle, right = [], [], []
#         for el in arr:
#             if el < pivot:
#                 left.append(el)
#             elif el == pivot:
#                 middle.append(el)
#             elif el > pivot:
#                 right.append(el)

#         return quicksort(left) + middle + quicksort(right)


# arr = quicksort([7, 9, 10, 1, 4, 5, 13, 87, 16, 4, 99, 5])
# print(arr)

# def sum_two(arr, target):
#     nums = set()
#     for el in arr:
#         pivot = target - el
#         if pivot in nums:
#             return [pivot, el]
#         else:
#             nums.add(el)
#     return None


# print(sum_two([1, 2, 3, 4, 5], 5))

# def maxProfit(prices):
#     if not prices or len(prices) == 1:
#         return 0

#     min_prices, max_profit = prices[0], 0

#     for i in range(1, len(prices)):
#         if prices[i] < min_prices:
#             min_prices = prices[i]
#         else:
#             max_profit = max(max_profit, prices[i] - min_prices)
#     return max_profit


# prices = [7, 1, 5, 3, 6, 4]
# print(maxProfit(prices))

# def containsDuplicate(nums):
#     return len(set(nums)) == len(nums)

# def containsDuplicate(nums):
#     hash = set()
#     for num in nums:
#         if not num in nums:
#             hash.add(num)
#         else:
#             return False
#     return True
# def productExceptSelf(nums):
#     length = len(nums)
#     result = [1] * length

#     left = 1
#     for i in range(length):
#         result[i] *= left
#         left *= nums[i]

#     rigth = 1
#     for i in range(length-1, -1, -1):
#         result[i] *= rigth
#         rigth *= nums[i]

#     return result


# nums = [1, 2, 3, 4]

# print(productExceptSelf(nums))


def maxSubArray(nums):
    max_sum = current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
