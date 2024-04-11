list1 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,0,0,0,0,0,0,2,2,2,2,2,2,4,4,4,4,4,4,6,6,6,6,6,6]

matrix_size = 3
matrix_column = 4
number_of_elements_array = 6
list_iterator = 0
ThreeD_list=[]
twoD_List = []

for i in range(matrix_size):
    outer_list = []
    for j in range(matrix_column):
        elements_appended = 0
        number_of_elements_list = []
        for k in range(list_iterator, len(list1)):
            elements_appended += 1
            number_of_elements_list.append(list1[k])
            if elements_appended==number_of_elements_array:
                outer_list.append(number_of_elements_list)
                list_iterator+=elements_appended
                break
    twoD_List.append(outer_list)
ThreeD_list.append(twoD_List)
print(ThreeD_list)