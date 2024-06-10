import random

def stochastic_hill_climbing(numbers):
    current_index = random.randint(0, len(numbers) - 1)
    current_max = numbers[current_index]
    iterations = 100 
    for _ in range(iterations):
        next_index = random.randint(0, len(numbers) - 1)
        if numbers[next_index] > current_max:
            current_max = numbers[next_index]
    return current_max

numbers = [1, 3, 7, 12, 9, 5]
max_number = stochastic_hill_climbing(numbers)
print("The maximum number in the list is:",max_number)

'''
output:
The maximum number in the list is: 12
'''
