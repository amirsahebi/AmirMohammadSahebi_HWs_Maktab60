import re

# defining a function checking if phone number has written in the right format
def phone_check(phone):
    # check the pattern of internal phone number and return that
    right_phone=re.search(".*(0|98)9[0-9]{9}\Z",phone)
    if right_phone:
        # replace the internal format by selected one
        edit_phone=re.sub(".*(0|98)","0",right_phone.group())
        print(edit_phone)
    else:
        print("invalid phone number!")

# phone_check("+989121111111")
# phone_check("+00989121111111")
# phone_check("09121111111")
# phone_check("+981121111111")
# phone_check("+0989121111111")


