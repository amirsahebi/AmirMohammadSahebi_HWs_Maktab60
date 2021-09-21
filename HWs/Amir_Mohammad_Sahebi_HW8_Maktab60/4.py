import re

# defining a function for checking "$" and digits and "A" in internal sentence
def sen_check(text):
    # search selected items in internal sentence
    check_1=re.search("\$",text)
    check_2=re.search("\d",text)
    check_3=re.search("A",text)
    # check if items exist or not
    if check_1 and check_2 and check_3:
        print("All items exist!")
    else:
        print("All items don't exist!")

# sen_check("Ali has 2$")