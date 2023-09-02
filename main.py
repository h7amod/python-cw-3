# P0
favorite_animals = ["dog", "cat", "monkey", "rabbit"]
print(favorite_animals)
print(favorite_animals[1])
favorite_animals.remove("monkey")

# P1
favorite_animals.append("elephant")
for animal in favorite_animals:
    print(f"I love {animal}")

# P2
numbers = [1, 2, 3, 4, 5]
numbers_sum = 0
for number in numbers:
    numbers_sum += number

print(numbers_sum)