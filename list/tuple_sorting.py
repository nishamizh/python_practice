#Write a Python program to get a sorted list in increasing order of last element in each tuple in a given list using loop.
#Input:- [(5,4),(9,1),(2,3),(5,9),(7,6),(5,5)]
#output:- [(9,1),(2,3),(5,4),(5,5),(7,6),(5,9)]

input_tuple = [(5,4),(9,1),(2,3),(5,9),(7,6),(5,5)]

for i in range(len(input_tuple)):
    for j in range(i+1,len(input_tuple)):
        if input_tuple[i][1] > input_tuple[j][1]:
            temp = input_tuple[i]
            input_tuple[i] = input_tuple[j]
            input_tuple[j] = temp

print(input_tuple)