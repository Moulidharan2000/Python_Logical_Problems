# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
# Example 1:
#
# Input: s = "hello"
# Output: "holle"
# Example 2:
#
# Input: s = "leetcode"
# Output: "leotcede"


def vowels_reverse(str1):
    # str3 = ""
    vowels = "aeiouAEIOU"
    # str2 = list(str1)
    # i, j = 0, len(str1) - 1
    # while i < j:
    #     if str2[i] not in vowels:
    #         i += 1
    #         continue
    #     if str2[j] not in vowels:
    #         j -= 1
    #         continue
    #     str2[i], str2[j] = str2[j], str2[i]
    #     i += 1
    #     j -= 1
    # for i in str2:
    #     str3 += i
    # print(str3)

    str1 = list(str1)
    str_vowels = iter([i for i in str1 if i in vowels][::-1])
    for i in range(len(str1)):
        if str1[i] in vowels:
            str1[i] = next(str_vowels)
    print("".join(str1))


if __name__ == '__main__':
    vowels_reverse("hello")
    vowels_reverse("lEetcode")
