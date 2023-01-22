dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

nums = dict(list(dic1.items()) + list(dic2.items()) + list(dic3.items()))
print("Original dictionary: ",nums)

total = sum(nums.values())
print("Sum of all the items in the dictionary: ", total)