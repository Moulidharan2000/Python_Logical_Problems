# [ "Apple" , "mAngo", "grapes"]
# [ "applE" , "mangO", "grapeS"]

def last_caps(str1_list):
    str2 = ''
    str2_list = []
    for i in str1_list:
        str2 = i
        str2 = str2[:len(i)-1].lower()+str2[-1].upper()
        str2_list.append(str2)
    print(str2_list)


if __name__ == '__main__':
    last_caps(["Apple", "mAngo", "grapes", "Jamun"])
