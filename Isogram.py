"""Function to check if string has repeating letters"""


def is_isogram(string):
    string=string.casefold()
    is_isogram= False
    counter=0
    if len(string)==0:
        is_isogram=True
    for i in string:
        if i != " " and i!="-":
            counter+=string.count(i)
        if i == " " or i=="-":
            counter+=1
    if counter < len(string)+1:
        is_isogram = True
    return is_isogram