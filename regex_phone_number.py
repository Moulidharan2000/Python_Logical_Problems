import re

# pattern = "^[6-9]{1}[0-9]{9}"
# phone_no = "7863257419"
# match = re.fullmatch(pattern, phone_no)
# if match:
#     print(True)
# else:
#     print(False)


email = 'sgfajh3156@gmail.com'
pattern = "^[a-z][0-9]+@[a-z]+[.a-z]{2, 5}"
pattern_match = re.fullmatch(pattern, email)
if pattern_match:
    print(True)
else:
    print(False)