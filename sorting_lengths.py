# Write a function that sorts a list of integers by their digit length in descending order, then settles ties by sorting numbers
# with the same digit length in ascending order.
#
# Examples
# digit_sort([77, 23, 5, 7, 101])
# ➞ [101, 23, 77, 5, 7]
#
# digit_sort([1, 5, 9, 2, 789, 563, 444])
# ➞ [444, 563, 789, 1, 2, 5, 9]
#
# digit_sort([53219, 3772, 564, 32, 1])
# ➞ [53219, 3772, 564, 32, 1]

def digit_sort(num_list):
    list2 = [str(i) for i in num_list]
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            if len(list2[i]) > len(list2[j]):
                list2[i], list2[j] = list2[j], list2[i]
            elif len(list2[i]) == len(list2[j]):
                if int(list2[i]) < int(list2[j]):
                    list2[i], list2[j] = list2[j], list2[i]
    num_list = [int(i) for i in list2]
    print(num_list)


if __name__ == '__main__':
    digit_sort([77, 23, 5, 7, 101, 110, 150])
    digit_sort([1, 5, 9, 2, 789, 563, 444])
    digit_sort([53219, 3772, 564, 32, 1])
