# Given Data Structures:
import random
data1 = (7, False, "Apple", True, 7, 98.6)
data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"}
data3 = ["A", 7, -1, 3.14, True, 7]
data4 = {"name": "Joe", "age": 26, "active": True, "hourly_wage": 14.75}

# Tasks Below;

# Data1: tuple

print(len(data1)) # Count the number of items 
print(data1[3]) # Find the value of the fourth item stored in the data set
print(data1.count(7)) # Count the number of times 7 appears

# Data2: set

data2.discard(random.choice(tuple(data2))) # Remove a random element from the data set
data2.add("Alpha")  # Add "Alpha" to the data set
print(data2) # Print data set.   My Note:can also, do this print(", ".join(str(item) for item in data2)) 


# Data3: list

data3.reverse() # Print the data set in reverse order
data3[1] = 'B' # Change the second value in the data set to ‘B’
removed_item = data3.pop() # Remove the last item and print the data set. # My Note: can also do this print(", ".join(str(item) for item in data3))
print(data3) 

# Data4: dictionary

data4["active"] = False # Change "active" to False
data4["address"] = "123 West Main Street" # Add "address" with a value of "123 West Main Street"
weekly_salary = data4["hourly_wage"] * 40 # Calculate weekly salary for Joe if he worked a full 40 hour week
print(weekly_salary)

print(data4) # Print the data set
