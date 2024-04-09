# List of pizza types for the task: "Think of at least three kinds of pizza"
pizzas = ["Margharita", "Pepperoni", "Bufalla"]

# Loop through the pizza list and print a sentence stating preference for each type
for pizza in pizzas:
    print(f"I like {pizza}")  # Task: "Modify the loop to display a sentence using that name"

# After the loop, print a statement that shows a general preference for pizza
print("I really like pizza")  # Task: "At the end of the program, include a sentence that shows your general preference for pizza"

# List of animals for the task: "Try to find three different animals with similar traits"
animals = ["Cat", "Dog", "Rabbit"]

# Loop through the animals list and print a statement about each animal
for animal in animals:
    print(f"{animal} is human great friend")  # Task: "Modify the program to display a statement about each animal"

# After the loop, print a sentence that shows a similarity between the previously mentioned animals
print("All animals mentioned are great!")  # Task: "At the end of the program, include a sentence indicating some similarity among the animals mentioned earlier"

# Use a for loop to display numbers from 1 to 20
for i in range(0,21):
    print(i)

# Create list of numbers from 1 to milion and display using for loop
list(i for i in range(1,1000001))

# Check if list is indeed starting at q and ending at milion
print(min((list(i for i in range(1,1000001)))))
print(max((list(i for i in range(1,1000001)))))

# Check how fast Python is summing all numbers in the list
print(sum((list(i for i in range(1,1000001)))))

# Using third function to range() function create list of odd numbers from 1 to 20 and display them using for loop
print(list(i for i in range(1,21,2)))

# Create list of numbers from 3 to 30 squared to the 3 power and display them using for loop
print(list(i**3 for i in range(3,31)))

# Create list of 10 first numbers to the power of 3
print(list(i**3 for i in range(1,11)))