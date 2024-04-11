#Write a Python program to find the list of words that are longer than or equal to 4 from a given string.
#Input:- 'How much wood would a woodchuck chuck if a woodchuck could chuck wood'
#Output:- ['much', 'wood', 'would', 'woodchuck', 'chuck', 'could']
#Note:- Duplicate should be avoided.

input_string = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood'
inp_lst = input_string.split()
out_lst = []

print(inp_lst)

for i in inp_lst:
    if len(i)>=4:
        if i not in out_lst:
            out_lst.append(i)

print(out_lst)