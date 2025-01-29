# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Find the symmetric difference using ^ operator
sym_diff1 = set1 ^ set2
print("Symmetric Difference using ^ operator:", sym_diff1)

# Find the symmetric difference using symmetric_difference() method
sym_diff2 = set1.symmetric_difference(set2)
print("Symmetric Difference using method:", sym_diff2)
