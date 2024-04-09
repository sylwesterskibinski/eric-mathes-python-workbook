# Create a list of places you would like to visit
places_to_visit = ["New York", "Tokyo", "Rome", "Rio", "Sydney"]

# Display the list
print(places_to_visit)

# Use the sorted() function to display the sorted list without changing the original order
print(sorted(places_to_visit))

# Display the original list again to show that it has not been changed by the sorted() function
print(places_to_visit)

# Use the sorted() function with the reverse parameter to display the list in reverse alphabetical order
print(sorted(places_to_visit, reverse=True))

# Use the reverse() method on the original list to reverse its order, and display the changed list
places_to_visit.reverse()
print(places_to_visit)

# Use the reverse() method again on the list to restore its original order
places_to_visit.reverse()
print(places_to_visit)

# Use the sort() method on the original list to sort it alphabetically and display the changes
places_to_visit.sort()
print(places_to_visit)

# Use the sort() method with the reverse parameter to sort the list in reverse alphabetical order and display the result
places_to_visit.sort(reverse=True)
print(places_to_visit)

print(len(places_to_visit))