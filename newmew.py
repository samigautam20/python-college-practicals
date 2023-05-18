set1 = set(input("Enter your values (comma separated): ").split(","))
set2 = set(input("Enter your values (comma separated): ").split(","))

new_set = set1.intersection(set2)
print(f"The common elements are {new_set}")