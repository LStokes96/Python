'''
A website requires the users to input username and password to register. Write a function to check the validity of password input by users.
	Following are the criteria for checking the password:
	- At least 1 letter between [a-z]
	- At least 1 number between [0-9]
	- At least 1 letter between [A-Z]
	- At least 1 character from [$#@]
	- Minimum length of transaction password: 6
	- Maximum length of transaction password: 12
Your program should accept a list of passwords of an indeterminate length and will check them according to the above criteria. Passwords that match the criteria are to be returned in a list.
	Example
	If the following passwords are given as input to the program:
	["ABd1234@1","a F1#","2w3E*","2We3345"]
	Then, the output of the program should be:
	["ABd1234@1"]
    '''
def password(list):
    final_list = []
    alpha = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    ALPHA = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    num = ["0","1","2","3","4","5","6","7","8","9"]
    char = ["$","#","@"]
    for each in range (len(list)):
        if len(list[each]) >= 6 and len(list[each]) <= 12:
            for a in range (len(alpha)):
                if alpha[a] in list[each]: 
                    for A in range(len(ALPHA)): 
                        if ALPHA[A] in list[each]:
                            for n in range (len(num)):
                                if num[n] in list[each]:
                                    for c in range(len(char)):
                                        if char[c] in list[each]:
                                            if list[each] not in final_list:
                                                final_list.append(list[each])
    return final_list

print(password(["ABd1234@1","a F1#","2w3E*","2We3345","Ybabc123$"]))    