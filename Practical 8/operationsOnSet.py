set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Intersection of sets
print("Intersection of sets:", set1.intersection(set2))

# Union of sets
print("Union of sets:", set1.union(set2))

# Set difference
print("Set difference (set1 - set2):", set1.difference(set2))

# Symmetric difference
print("Symmetric difference:", set1.symmetric_difference(set2))

# Clearing a set
set1.clear()
print("Cleared set:", set1)
