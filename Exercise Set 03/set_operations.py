set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

difference_set1 = set1 - set2
difference_set2 = set2 - set1

union_set = set1 | set2

symmetric_difference1 = set1 ^ set2
symmetric_difference2 = set2 ^ set1

set_intersection1  = set1 & set2
set_intersection2  = set2 & set1

# Set of Difference
print("Set Difference")
print(f"set1 - set 2 = ", difference_set1)
print(f"set2 - set 1 = ", difference_set2)

# Union of Sets
print(f"Union of Sets: ", union_set)

#Symmetric Difference
print("Symmetric Difference")
print(f"set1 ^ set 2 = ", symmetric_difference1)
print(f"set2 ^ set 1 = ", symmetric_difference2)

#Set Intersection
print("Set Intersection")
print(f"set1 & set 2 = ", set_intersection1)
print(f"set2 & set 1 = ", set_intersection2)