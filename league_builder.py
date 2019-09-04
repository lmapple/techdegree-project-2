"""
lmapple
Python Web Development Techdegree
Project 2 - Build a Soccer League
--------------------------------
Objectives:
1. In your Python program, read the data from the supplied CSV file.
   Store that data in an appropriate data type so that it can be used
   in the next task.
2. Create logic that can iterate through all 18 players and assign them
   to teams such that each team has the same number of players. The number
   of experienced players on each team should also be the same.
3. Finally, the program should output a text file named -- teams.txt -- that
   contains the league roster listing the team name, and each player on the team
   including the player's information: name, whether they've played soccer before
   and their guardians' names.
--------------------------------
"""
#Attempting "Exceeds Expectations" grade.

#Script should be named league_builder.py.
#Ensure that the script does not execute when imported.

if __name__ == '__main__':

    import csv
    import random

#Create blank team lists and counter variables.

    dragons = []
    sharks = []
    raptors = []
    dragons_experienced_players = int(0)
    sharks_experienced_players = int(0)
    raptors_experienced_players = int(0)

#Read the csv file with the player information and save as a list of dictionaries.

    with open('soccer_players.csv', newline = '') as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter=',')
        player_rows = list(player_reader)

#For each player row from the file, generate a random number and assign to a team, taking
#experience into account. There will be three equal teams in both number and skill level.

        for row in player_rows:
            random_number = random.randint(1,3)

#Ensure the teams maintain a relatively equal number of overall players while assigning
#the inexperienced players.
      
            if row['Soccer Experience'] == "NO":

                if random_number == 1:
                    if len(dragons) <= len(sharks) and len(dragons) <= len(raptors):
                        dragons.append(row)
                        row['Team'] = 'Dragons'
                    else:
                        if len(sharks) <= len(raptors):
                            sharks.append(row)
                            row['Team'] = 'Sharks'
                        else:
                            raptors.append(row)
                            row['Team'] = 'Raptors'

                elif random_number == 2:
                    if len(sharks) <= len(dragons) and len(sharks) <= len(raptors):
                        sharks.append(row)
                        row['Team'] = 'Sharks'
                    else:
                        if len(dragons) <= len(raptors):
                            dragons.append(row)
                            row['Team'] = 'Dragons'
                        else:
                            raptors.append(row)
                            row['Team'] = 'Raptors'

                elif random_number == 3:
                    if len(raptors) <= len(dragons) and len(raptors) <= len(sharks):
                        raptors.append(row)
                        row['Team'] = 'Raptors'
                    else:
                        if len(dragons) <= len(sharks):
                            dragons.append(row)
                            row['Team'] = 'Dragons'
                        else:
                            sharks.append(row)
                            row['Team'] = 'Sharks'

            else:            

#Ensure the teams maintain a relatively equal number of experienced players.

                if random_number == 1:
                    if dragons_experienced_players <= sharks_experienced_players and dragons_experienced_players <= raptors_experienced_players:
                        dragons.append(row)
                        dragons_experienced_players += 1
                        row['Team'] = 'Dragons'
                    else:
                        if sharks_experienced_players <= raptors_experienced_players:
                            sharks.append(row)
                            sharks_experienced_players += 1
                            row['Team'] = 'Sharks'
                        else:
                            raptors.append(row)
                            raptors_experienced_players += 1
                            row['Team'] = 'Raptors'

                elif random_number == 2:
                    if sharks_experienced_players <= dragons_experienced_players and sharks_experienced_players <= raptors_experienced_players:
                        sharks.append(row)
                        sharks_experienced_players += 1
                        row['Team'] = 'Sharks'
                    else:
                        if dragons_experienced_players <= raptors_experienced_players:
                            dragons.append(row)
                            dragons_experienced_players += 1
                            row['Team'] = 'Dragons'
                        else:
                            raptors.append(row)
                            raptors_experienced_players += 1
                            row['Team'] = 'Raptors'

                elif random_number == 3:
                    if raptors_experienced_players <= dragons_experienced_players and raptors_experienced_players <= sharks_experienced_players:
                        raptors.append(row)
                        raptors_experienced_players += 1
                        row['Team'] = 'Raptors'
                    else:
                        if dragons_experienced_players <= sharks_experienced_players:
                            dragons.append(row)
                            dragons_experienced_players += 1
                            row['Team'] = 'Dragons'
                        else:
                            sharks.append(row)
                            sharks_experienced_players += 1
                            row['Team'] = 'Sharks'

#Write the new team information to a text file named "teams.txt".
#List the player name, whether the player has soccer experience,
#and the player's guardian names. Separate all with a comma.
#Overwrite file in case the teams are regenerated later.

    with open("teams.txt","w") as file:
        file.write("Soccer League Team Rosters:"+"\n"+"\n"+"\n"
                   +"Dragons"+"\n"+"="*7+"\n")

        for player in dragons:
            file.write(player["Name"]+","
                       + player["Soccer Experience"]+","
                       + player["Guardian Name(s)"]+"\n")

        file.write("\n"+"\n"+"Sharks"+"\n"+"="*7+"\n")

        for player in sharks:
            file.write(player["Name"]+","
                       + player["Soccer Experience"]+","
                       + player["Guardian Name(s)"]+"\n")

        file.write("\n"+"\n"+"Raptors" + "\n" + "=" * 7 + "\n")

        for player in raptors:
            file.write(player["Name"]+","
                       + player["Soccer Experience"]+","
                       + player["Guardian Name(s)"]+"\n")

#Create welcome letters to the player guardians. There will be one
#text file per player. Include the player's name, team name, and
#date & time of the first practice.

    def guardian_letters(team):
        for player in team:
            first_name, last_name = player["Name"].lower().split(" ")
            with open(first_name + "_" + last_name + ".txt","w") as file:
                file.write("Dear " + player["Guardian Name(s)"] + "," + "\n"*2
                           +"Congratulations! Your child, " + player["Name"]
                           +", has been assigned to play for the " + player["Team"] +".\n"
                           +"The first practice will be held on 10/1/2019 at 5:00 PM.\n"
                           +"We look forward to a great season!" + "\n"*2 + "Regards."
                           )

    guardian_letters(dragons)
    guardian_letters(sharks)
    guardian_letters(raptors)