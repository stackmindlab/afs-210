# Python Data Structures:

# Given Data Structures:
import random
data1 = [7, False, "Apple", True, 7, 98.6]
data2 = ["July", 4, 8, "Tango", 4.3, "Bingo"]
data3 = ["A", 7, -1, 3.14, True, 7]
data4 = {"name": "Joe", "age": 26, "active": True, "hourly_wage": 14.75}

# Tasks: Below ---->

# Data1:
# Count the number of items
print(len(data1))
# Find the value of the fourth item stored in the data set
print(data1[3])
# Count the number of times 7 appears
print(data1.count(7))

# Data2:
# Remove a random element from the data set
data2.pop(random.randrange(len(data2)))
 # Add "Alpha" to the data set
data2.append("Alpha") 
# Print data set
print(data2) # Note:can also, do this  print(", ".join(str(item) for item in data2)) 


# Data3:
# Print the data set in reverse order
data3.reverse()
# Change the second value in the data set to ‘B’
data3[1] = 'B'
# Remove the last item and print the data set
removed_item = data3.pop() 
print(data3) # Note: can also do this print(", ".join(str(item) for item in data3))

# Data4:
# Change "active" to False
data4["active"] = False 
# Add "address" with a value of "123 West Main Street"
data4["address"] = "123 West Main Street"
# Calculate weekly salary for Joe if he worked a full 40 hour week
weekly_salary = data4["hourly_wage"] * 40
print(weekly_salary)

# Print the data set
print(data4)
