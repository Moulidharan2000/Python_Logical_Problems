# The function is given two strings t - template, s - to be sorted.
# Sort the characters in s such that if the character is present in t then it is sorted according to the
# order in t and other characters are sorted alphabetically after the ones found in t.
#
# Examples
# custom_sort("edc", "abcdefzyx") ➞ "edcabfxyz"
#
# custom_sort("fby", "abcdefzyx") ➞ "fbyacdexz"
#
# custom_sort("", "abcdefzyx") ➞ "abcdefxyz"
#
# custom_sort("", "") ➞ ""
# Notes
# The characters in t and s are all lower-case.


def custom_sort(str_t, str_s):
    str_s1 = ""
    for i in str_s:
        if i in str_t:
            pass
        else:
            str_s1 += i
    str_s1 = sorted(str_s1)
    sorted_s1 = ""
    for i in str_s1:
        sorted_s1 += i
    sorted_ts = str_t+sorted_s1
    print(sorted_ts)


if __name__ == '__main__':
    custom_sort("edc", "abcdefzyx")
    custom_sort("fby", "abcdefzyx")
    custom_sort("", "abcdefzyx")
    custom_sort("", "")
