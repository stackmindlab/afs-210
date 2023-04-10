import random

sample_input = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

# Time complexity is: O(n)
# This algorithm iterates over the list once and performs a constant amount of work for each position.
def custom_shuffle(my_list):
    for current_index in range(len(my_list)-1, 0, -1):
        random_index = random.randint(0, current_index)
        my_list[current_index], my_list[random_index] = my_list[random_index], my_list[current_index]
    return my_list

print("Before Shuffle:")
print(sample_input)

print("Shuffled lists:")

for i in range(5):
    shuffled_list = custom_shuffle(sample_input)
    print(shuffled_list)


