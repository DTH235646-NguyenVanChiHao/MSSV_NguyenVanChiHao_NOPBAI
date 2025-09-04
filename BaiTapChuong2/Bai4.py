# Python Program: Demonstrating Basic Data Types

# 1. Numeric Types
int_num = 10             # int
float_num = 3.14         # float
complex_num = 2 + 3j     # complex

print("Integer:", int_num, "Type:", type(int_num))
print("Float:", float_num, "Type:", type(float_num))
print("Complex:", complex_num, "Type:", type(complex_num))

print("-" * 40)

# 2. String
text = "Hello Python"
print("String:", text, "Type:", type(text))

print("-" * 40)

# 3. Boolean
is_active = True
print("Boolean:", is_active, "Type:", type(is_active))

print("-" * 40)

# 4. Collections
# List
my_list = [1, 2, 3, "apple"]
print("List:", my_list, "Type:", type(my_list))

# Tuple
my_tuple = (1, 2, 3, "banana")
print("Tuple:", my_tuple, "Type:", type(my_tuple))

# Set
my_set = {1, 2, 3, 2}
print("Set:", my_set, "Type:", type(my_set))  # Duplicates removed

# Frozen Set
my_frozenset = frozenset([1, 2, 3, 3])
print("FrozenSet:", my_frozenset, "Type:", type(my_frozenset))

# Dictionary
my_dict = {"name": "T-Hao", "age": 20}
print("Dictionary:", my_dict, "Type:", type(my_dict))

print("-" * 40)

# 5. NoneType
nothing = None
print("NoneType:", nothing, "Type:", type(nothing))
