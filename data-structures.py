name = "titus"
# print(name.capitalize())

# for n in name:
#     print(n)

# for n in range(0, 30, 2):
#     print(n)

# fruits = ["apple", "mango", "orange", "kiwi"]

# # print(dir(fruits))

# print(len(fruits))
# fruits.clear()
# print(fruits)
    
numbers  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_numbers = []

for num in numbers:
    if num % 2 == 0:
        new_numbers.append(num)

# print(new_numbers)

# list compression

even_list = [num for num in numbers if num % 2 == 0]

print(even_list)

squred_numbers = [n**2 for n in numbers]

print(squred_numbers)