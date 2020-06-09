def alpha(word_list):
    list = word_list.split(',')
    sorted_list = sorted(list, key=str.lower)
    string1 = ""
    for i in sorted_list:
        string1 += i + ","
    return string1

word_list = "this,About,could,ZOO"
print(alpha(word_list))