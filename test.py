def even_number(nums):
    result = []
    nums   = list(range(50))
    for i in nums:
        if i % 2 == 0:
            result.append(i+1)
    return result
