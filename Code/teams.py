#Create a Python file which does the following:
#Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
#Reads and displays the names of the 1st and 4th team in the file.
#Create a new Python file which does the following:
#Edits your "teams.txt" file so that the top line is replaced with "This is a new line".
#Print out the edited file line by line.
teams_file = open("teams.txt", "w")
teams_1 = str(input("Name a team: "))
teams_2 = str(input("Name a team: "))
teams_3 = str(input("Name a team: "))
teams_4 = str(input("Name a team: "))
teams_5 = str(input("Name a team: "))

teams_file.write(teams_1 + "\n")
teams_file.write(teams_2 + "\n")
teams_file.write(teams_3 + "\n")
teams_file.write(teams_4 + "\n")
teams_file.write(teams_5 + "\n")
teams_file.close()

teams_file = open("teams.txt", "r")
print(teams_file.readline())
teams_file.readline()
teams_file.readline()
print(teams_file.readline())
teams_file.close()