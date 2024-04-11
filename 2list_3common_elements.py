#Write a Python program which takes two list as input and returns True if they have at least 3 common elements.
#Output:- True

inp_lst1 = eval(input('Enter List1: ')) #[10,20,'Python', 10.20, 10+20j, [10,20,30], (10,20,30)]
inp_lst2 = eval(input('Enter List2: ')) #[(10,20,30),1,20+3j,100.2, 10+20j, [10,20,30],'Python']

counter = 0
output = False

for i in inp_lst2:
    if i in inp_lst1:
        counter+=1
        if counter==3:
            output= True
            break

print(output)