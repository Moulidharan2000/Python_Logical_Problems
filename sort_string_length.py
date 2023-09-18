# Create a function that takes a string and returns a string ordered by the length of the words.
# From shortest to longest word. If there are words with the same amount of letters, order them alphabetically.
#
# Examples
# sort_by_length("Hello my friend") ➞ "my Hello friend"
#
# sort_by_length("Have a wonderful day") ➞ "a day Have wonderful"
#
# sort_by_length("My son loves pineapples") ➞ "My son loves pineapples"\

def sort_string(str1):
    str1_list = str1.split(" ")
    for i in range(len(str1_list)):
        for j in range(len(str1_list)):
            if len(str1_list[i]) < len(str1_list[j]):
                str1_list[i], str1_list[j] = str1_list[j], str1_list[i]
    str2 = ""
    for i in str1_list:
        str2 += i+" "
    print(str2)


if __name__ == '__main__':
    sort_string("Hello my friend")
    sort_string("Have a wonderful day")
    sort_string("My son loves pineapples")
