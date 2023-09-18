list1 = [7, 2, 90, 10, 75]
list2 = sorted(list1)
print(list1)
# list3 = []
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i] == list2[j]:
#             list3.append(j+1)

list3 = [j+1 for i in range(len(list1)) for j in range(len(list2)) if list1[i] == list2[j]]
print(list3)
