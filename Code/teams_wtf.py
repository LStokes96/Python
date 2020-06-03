change_teams = open("teams.txt", "r")
all_lines = change_teams.readlines()
all_lines[0] = "This is a new line\n"

change_teams = open("teams.txt", "w")
change_teams.writelines(all_lines)

change_teams.close()

change_teams = open("teams.txt","r")
print(change_teams.read())
change_teams.close()