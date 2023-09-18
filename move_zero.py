def zeros_move(list1):
    non_zeros = [x for x in list1 if x != 0]
    zeros = [j for j in list1 if j == 0]
    non_zeros.extend(zeros)
    print(non_zeros)


if __name__ == '__main__':
    zeros_move([0, 1, 0, 3, 12])
    zeros_move([1, 7, 0, 0, 8, 0, 10, 12, 0, 4])
