import pdb


def Near(string_1,string_2):
    
    string_len = len(string_1)
    
    for x in range (0,string_len):
        string_3 = string_1[:x:] + string_1[x+1::]
        
        if string_3 == string_2:
            return True
        elif x == string_len:
            return False
        elif string_3 != string_2:
            continue
        else:
            return False

print(Near("Hello","Hell"))
