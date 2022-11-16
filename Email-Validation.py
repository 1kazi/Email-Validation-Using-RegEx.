# a-z      azcube@gmail.com
# 0-9
# . _ at the only one
# @ contain only one time
# . is present at the 2nd  and 3red  position from the last

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your Email::   ")

if re.search(email_condition, user_email):
    print(" Right Email  ")
else:
    print(" Wrong email ")
