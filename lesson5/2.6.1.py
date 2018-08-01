import random
import string

# generate list of symbols
dig = [1, 2, 3, 4, 5, 6, 7, 8, 0]
dig.extend(list(string.ascii_letters))
set1 = {_ for _ in random.sample(dig, k=20)}
set2 = { _ for _ in random.sample(dig, k=20)}

print("First set:", set1)
print("Second set:", set2)
tup_intersection = tuple(set1 & set2)
print("Intersection:", tup_intersection)
tup_difference = tuple(set1-set2)
print("Difference first set and second set:", tup_difference)
print("Slice first 3 symbols from first tuple:", tup_intersection[:3])
print("Revers intersection:", tup_intersection[::-1])
list_intersection = list(tup_intersection)
list_difference = list(tup_difference)
print("List intersection:", list_intersection)
print("List difference:", list_difference)