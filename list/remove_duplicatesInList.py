# Write a Python program to remove duplicate element from a list using loop.
# Input:- [10,1,11,1,29,876,768,10,11,1,92,29,876]
# Output:- [10,1,11,29,876,768,92]

input_dup = [10, 1, 11, 1, 29, 876, 768, 10, 11, 1, 92, 29, 876]
list_backup = []

for i in range(len(input_dup)):
    if input_dup[i] not in list_backup:
        list_backup.append(input_dup[i])

print(list_backup)
