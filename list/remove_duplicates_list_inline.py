# Write a Python program to remove duplicate element from a list using loop.
# Input:- [10,1,11,1,29,876,768,10,11,1,92,29,876]
# Output:- [10,1,11,29,876,768,92]

input_dup = [10, 1, 11, 1, 29, 876, 768, 10, 11, 1, 92, 29, 876]
list_backup = []

counter=0
for i in range(1,len(input_dup)-counter):
    counter+=1
    if input_dup[i] in input_dup:
        input_dup.remove(input_dup[i])

print(input_dup)

# Note: not completed