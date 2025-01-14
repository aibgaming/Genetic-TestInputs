# two_sum.py
def two_sum(nums, target):
    """
    Returns the indices of two numbers that add up to the target.
    """
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
    return []
