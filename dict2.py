dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

nums = dict(list(dic1.items()) + list(dic2.items()) + list(dic3.items()))

print("Original dictionary: ",nums)

maximum_value = max(nums.values())
minimum_value = min(nums.values())

print("Maximum value in the dictionary: ", maximum_value)
print("Minimum value in the dictionary: ", minimum_value)