import string


def missing(unique_str):
    alphabet_str = list(string.ascii_lowercase)
    missing_str = ""
    for i in alphabet_str:
        if i not in unique_str:
            missing_str += i
    print(missing_str)


if __name__ == '__main__':
    missing("abcdefgpqrstuvwxyz")
    missing("zyxwvutsrq")
    missing("defghijklmnopqrstuvwxyz")
    missing("abcdefghijklmnopqrstuvwxyz")
