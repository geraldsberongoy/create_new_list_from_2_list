# Exercise 10: Create a new list from two list using the following condition

# Given:
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# Expected Output:
# result list: [25, 35, 40, 60, 90]

# Pseudocode
# assignning variable to two list
# assigning empty variable for result_list
# for loop with nested conditional to add the odd first list in result list
# another for loop with nested conditional to add the even second list in result list
# print result list

# # # CODE # # #

# Given List
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
result_list = []

# For loop
for i in list1:
    if i % 2 != 0:
        result_list.append(i)
for i in list2:
    if i % 2 == 0:
        result_list.append(i)

# Print lists   
print(f"The first list: {list1}")
print(f"The second list: {list2}")
print(f"Result list: {result_list}")