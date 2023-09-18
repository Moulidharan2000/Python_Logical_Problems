# Given two arrays of positive integers, add their elements into a new array.
# The solution should add both arrays, one by one starting from the 0'th index,
# and split the sum into individual digits if it is a 2–digit number.
#
# Input : [23, 5, 2, 7, 87], [4, 67, 2, 8]
# Output: [2, 7, 7, 2, 4, 1, 5, 8, 7]
#
# Input : [], [4, 67, 2, 8]
# Output: [4, 6, 7, 2, 8]

def add_split(list1, list2):
    list3 = []
    if len(list1) > len(list2):
        for i in range(len(list2), len(list1)):
            list2.append(0)
    elif len(list2) > len(list1):
        for i in range(len(list1), len(list2)):
            list1.append(0)
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        list3.append(list1[i] + list2[j])
        i += 1
        j += 1
    list3 = [int(i) if i.isdigit() else i for j in list3 for i in str(j)]
    print(list3)


if __name__ == '__main__':
    add_split([23, 5, 2, 7, 87], [4, 67, 2, 8])
    add_split([], [4, 67, 2, 8])
