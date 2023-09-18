# [2, 1, 4, 3]

def swap(num_list):
    rem = len(num_list) % 4
    length = len(num_list)-rem
    for i in range(0, length, 4):
        temp1, temp2 = num_list[i], num_list[i+1]
        num_list[i], num_list[i + 1] = num_list[i + 2], num_list[i + 3]
        num_list[i+2], num_list[i+3] = temp1, temp2
    print(num_list)


swap([2, 1, 4, 3, 5, 7, 8, 9, 10, 8, 9, 7, 2])
