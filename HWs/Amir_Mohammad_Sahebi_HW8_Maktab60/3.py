import re

# defining a function for searching a word at last of sentence
def ch_exist(word,text):
    # use search method and defining a pattern with "\Z" that use for searching word at last of sentence 
    exist=re.search(f"{word}\Z",text)
    if exist:
        print("The word exist at the end of sentence!")
    else:
        print("The word doesn't exist at the last of sentence!")

ch_exist("python","it's interesting to see growth in python")