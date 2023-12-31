# Create a function which takes every letter in every word, and puts it in alphabetical order.
# Note how the original word lengths must stay the same.
#
# Examples
# true_alphabetic("hello world") ➞ "dehll loorw"
#
# true_alphabetic("edabit is awesome") ➞ "aabdee ei imosstw"
#
# true_alphabetic("have a nice day") ➞ "aaac d eehi nvy"
# Notes
# All sentences will be in lowercase.
# No punctuation or numbers will be included in the Tests.


def true_alphabetic(str1):
    str2 = sorted(str1)
    str3 = ""
    for i in str2:
        str3 += "".join(sorted(i))
    print(str3)


if __name__ == '__main__':
    true_alphabetic("hello world")
    true_alphabetic("edabit is awesome")
    true_alphabetic("have a nice day")
