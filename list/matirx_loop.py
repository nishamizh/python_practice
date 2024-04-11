#2X2 matrix
list1 = [0, 0, 0, 0, 0, 1, 2, 3, 0, 2, 4, 6, 0, 3, 6, 9]

outer_list = []
outer_counter = 0
counter = 0
for i in range(0, 4):
    list_inner = []
    for j in range(outer_counter,len(list1)):
        print(j)
        list_inner.append(list1[j])
        counter += 1
        if counter == 4:
            outer_counter +=counter
            counter = 0
            outer_list.append(list_inner)
            break

print(outer_list)