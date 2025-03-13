# WAP to find the sum of all items in a dictionary
# Input: {'a': 100, 'b':200, 'c':300}
# Output: 600
# Input: {'x': 25, 'y':18, 'z':45}
# Output: 88


user_dict = {}

sum = 0

num_items = int(input("Enter the number of items in the dictionary: "))

for _ in range(num_items):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    user_dict[key] = value

print("The dictionary is:", user_dict)

# Iteration over values
for value in user_dict.values():
    sum = sum + int(value)

print(sum)
