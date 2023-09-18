# import math
#
#
# def factors(num):
#     while num % 2 == 0:
#         print(2)
#         num = num / 2
#     for i in range(3, int(math.sqrt(num)) + 1, 2):
#         while num % i == 0:
#             print(i)
#             num = num / i
#     if num > 2:
#         print(num)
#
#
# if __name__ == '__main__':
#     num = int(input("Enter the number : "))
#     factors(num)

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list1)
# [3,4,1,2,7,8,5,6]
length = int(len(list1) / 2)
print(length)
# for i in range(length):
#     for j in range(length):
#         if list1[i] > list1[j]:
#             (list1[i], list1[j]) = (list1[j], list1[i])
# print(list1)
for i in range(len(list1)):
    for j in range(len(list1)):
        temp = list1[i]
        list1[i] = list1[j]
        list1[j] = temp
for i in range(length, len(list1)):
    for j in range(length, len(list1)):
        temp = list1[i]
        list1[i] = list1[j]
        list1[j] = temp
print(list1)

