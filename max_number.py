def max_min(list_1):
    for i in range(len(list_1)):
        for j in range(len(list_1)):
            if list_1[i] < list_1[j]:
                temp = list_1[i]
                list_1[i] = list_1[j]
                list_1[j] = temp
    print(list_1)
    maximum = list_1[len(list_1)-1]
    minimum = list_1[0]
    # for i in range(len(list_1)):
    #     for j in range(len(list_1)):
    #         if list_1[i] > list_1[j]:
    #             maximum = list_1[i]
    print("Max : ", maximum)
    print("Min : ", minimum)


if __name__ == '__main__':
    list_1 = [1, 5, 100, 8, 250, 3, 99, 120]
    max_min(list_1)

