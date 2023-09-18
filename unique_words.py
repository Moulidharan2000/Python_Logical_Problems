# Create a function that takes in two words as input and returns a list of three elements, in the following order:
# Shared letters between two words.
# Letters unique to word 1.
# Letters unique to word 2.
# Each element should have unique letters, and have each letter be alphabetically sorted.
# Examples
# letters("sharp", "soap") ➞ ["aps", "hr", "o"]
#
# letters("board", "bored") ➞ ["bdor", "a", "e"]
#
# letters("happiness", "envelope") ➞ ["enp", "ahis", "lov"]
#
# letters("kerfuffle", "fluffy") ➞ ["flu", "ekr", "y"]
# # Even with multiple matching letters (e.g. 3 f's), there should
# # only exist a single "f" in your first element.
#
# letters("match", "ham") ➞ ["ahm", "ct", ""]
# # "ham" does not contain any letters that are not found already
# # in "match".
# Notes
# Both words will be in lower case.
# You do not have to worry about punctuation, all words only have letters from [a-z].
# If an element contains no letters, return an empty string (see last example).

def unique_words(str1, str2):
    sorted_str1 = sorted(set(sorted(str1)))
    sorted_str2 = sorted(set(sorted(str2)))
    str3 = ""
    str4 = ""
    str5 = ""
    unique_list = []
    for i in sorted_str1:
        if i in sorted_str2:
            str3 += i
        else:
            str4 += i
    unique_list.append(str3)
    unique_list.append(str4)
    for i in sorted_str2:
        if i not in sorted_str1:
            str5 += i
    unique_list.append(str5)
    print(unique_list)


if __name__ == '__main__':
    unique_words("sharp", "soap")
    unique_words("board", "bored")
    unique_words("happiness", "envelope")
    unique_words("kerfuffle", "fluffy")
    unique_words("match", "ham")
