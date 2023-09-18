# def secondlargest(list1):
#     largest = 0
#     second_largest = 0
#     for i in range(len(list1)):
#         if largest < list1[i]:
#             largest = list1[i]
#         if second_largest < largest:
#             if second_largest < list1[i] and list1[i] < largest:
#                 second_largest = list1[i]
#     print(largest)
#     print(second_largest)
#
#
# if __name__ == '__main__':
#     list1 = [18, 4, 10, 13, 11, 12]
#     secondlargest(list1)
#
#
#

class Demo:

    def sample1(self):
        return "sample1"

    def __sample2(self):
        return "sample2"

    def _sample3(self):
        return "sample3"


demo = Demo()
print(demo.sample1())
print(demo.__sample2())
print(demo._sample3())
