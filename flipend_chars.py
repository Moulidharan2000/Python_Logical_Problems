str1 = "Cat, dog, and mouse."
#str1 = "A"
if len(str1) < 2:
    print("incompatible")
else:
    if str1[0] == str1[-1]:
        print("Two's a pair")
    else:
        str2 = str1[-1] + str1[1:len(str1)-1:] + str1[0]
        print(str2)
