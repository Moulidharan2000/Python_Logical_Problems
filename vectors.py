# The goal is to test if a consecutive sequence is formed.
# A consecutive sequence is defined as sequence of incrementing numbers (e.g. 1, 2, 3 or 5, 6, 7, 8).
# The twist is that you have to consider the combination of vectors as shown.
#
# [3 5 1 -5 ]  =>  [3+4  5+3  1+8  15-5]  =  [7 8 9 10]  =>  true
# [4 3 8 15]
# Also important is that the vectors can be of different sizes, where excess numbers in the longer one will be paired with 0s from the other one.
#
# [2 2 2  ]  =>  [2+5  2+6  2+7  10+0]  = [ 7 8 9 10]  =>  true
# [5 6 7 10]
# Notes
# Each array has at least two elements.


def order_sequence(list1, list2):
    if len(list1) > len(list2):
        for i in range(len(list2), len(list1)):
            list2.append(0)
    elif len(list2) > len(list1):
        for i in range(len(list1), len(list2)):
            list1.append(0)
    sequence_list = [list1[i] + list2[i] for i in range(len(list1))]
    print(sequence_list)
    for i in range(len(sequence_list)-1):
        if not sequence_list[i+1] - sequence_list[i] == 1:
            return False
    return True


if __name__ == '__main__':
    print(order_sequence([3, 5, 1, -5], [4, 3, 8, 15]))
    print(order_sequence([2, 2, 2], [5, 6, 7, 10]))
