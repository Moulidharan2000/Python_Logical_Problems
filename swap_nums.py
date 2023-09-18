def swap(a, b):
    num_list = []
    num_list.append(a)
    num_list.append(b)
    a = num_list[1]
    b = num_list[0]
    print("a = ", a, " b = ", b)


if __name__ == '__main__':
    a = 10
    b = 5
    swap(a, b)
