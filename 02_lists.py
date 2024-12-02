def get_even_nums(nums):
    arr_returned_nums = []

    for num in nums:
        if ((num % 2) == 0):
            arr_returned_nums.append(num)

    return arr_returned_nums

print(get_even_nums([1, 2, 3, 5]))

def get_items_longer_than(strs, max_len):
    arr_returned_strings = []

    for string in strs:
        if (len(string) > max_len): 
            arr_returned_strings.append(string)
    
    return arr_returned_strings

print(get_items_longer_than(['a', 'bb', 'ccc'], 1))
print(get_items_longer_than(['a', 'bb', 'ccc'], 2))
print(get_items_longer_than(['a', 'bb', 'ccc'], 4))
print(get_items_longer_than(['a', 'bb'], 0))
print(get_items_longer_than(['a', 'bb'], 3))
print(get_items_longer_than(['a', 'bb', 'ccc'], 2))

