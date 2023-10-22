import sys

def get_memory_size(obj):
    return sys.getsizeof(obj)

# Example usage:
obj1 = "龘"
obj2 = 123
obj3 = [1, 2]
obj4 = (1, 2)

print(get_memory_size(obj1))  # Output: 76
print(get_memory_size(obj2))  # Output: 28
print(get_memory_size(obj3))  # Output: 72
print(get_memory_size(obj4))  # Output: 56
