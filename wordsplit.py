# Have the function ArrayChallenge(strArr) read the array of strings stored in strArr,
# which will contain 2 elements: the first element will be a sequence of characters,
# and the second element will be a long string of comma-separated words,
# in alphabetical order, that represents a dictionary of some arbitrary length.
# For example: strArr can be: ["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"].
# Your goal is to determine if the first element in the input can be split into two words,
# where both words exist in the dictionary that is provided in the second input.
# In this example, the first element can be split into two words:
# hello and cat because both of those words are in the dictionary.

# Your program should return the two words that exist in
# the dictionary separated by a comma. So for the example above,
# your program should return hello,cat. There will only be one correct
# way to split the first element of characters into two words.
# If there is no way to split string into two words that exist
# in the dictionary, return the string not possible. The first
# element itself will never exist in the dictionary as a real word. 


def funfun(strArr):
    cmpo_wrd = strArr[0]
    word_dic = strArr[1].split(',')

    for i in word_dic:
        cond1 = cmpo_wrd.startswith(i)
        cond2 = cmpo_wrd[len(i):] in word_dic
        # print(i, cmpo_wrd[len(i):])
        # print(cond1, cond2)
        if cond1 and cond2:
            return f'{i},{cmpo_wrd[len(i):]}'
    return "not possible"


print(funfun(["hellocat", "apple, bat,cat,goodbye,hello,yellow,why"]))
print(funfun(["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]))
print(funfun(["abcgefd", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"]))
