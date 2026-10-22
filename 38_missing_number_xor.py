def find_missing_number(nums):
    n = len(nums) + 1
    xor_total = 0
    for i in range(1, n + 1):
        xor_total ^= i
    for num in nums:
        xor_total ^= num
    return xor_total