# Given three lists of integers: lst1, lst2, lst3, return the sum of integers which are common in all three lists.
#
# Examples
# sum_common([1, 2, 3], [5, 3, 2], [7, 3, 2]) ➞ 5
# // 2 & 3 are common in all 3 lists.
#
# sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]) ➞ 7
# // 2, 2 & 3 are common in all 3 lists.
#
# sum_common([1], [1], [2]) ➞ 0

def sum_values(list1, list2, list3):
    sum_common = 0
    for i in list1:
        if i in list2 and i in list3:
            sum_common += i
    print(sum_common)


if __name__ == '__main__':
    sum_values([1, 2, 3], [5, 3, 2], [7, 3, 2])
    sum_values([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2])
    sum_values([1], [1], [2])



