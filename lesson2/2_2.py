import math
import random

int_seq = random.choices(range(0,100),k=5)
float_random = random.random() * 100
print("Random integer sequence: ", int_seq)
print("Random float number: ", float_random)

int_seq_max = max(int_seq)
print("Maximum from integer sequence: ", int_seq_max)

floor_div_result = int_seq_max // float_random
print("Result floor division :", floor_div_result)

print("Factorial from result floor division", math.factorial(floor_div_result))