"""I'm sure there is a better way of doing this..."""

import constants
import copy

def team_cleaner():
    """This function will create a new list for using, and change the information as needed in the rubric"""
    #new list
    clean_list = copy.deepcopy(constants.PLAYERS)
    #function to clean per rules
    loop_start = 0
    loop_end = (len(constants.PLAYERS))
    while loop_start != loop_end:
        clean_list[loop_start]['height'] = clean_list[loop_start]['height'].removesuffix(" inches")
        clean_list[loop_start]['height'] = int(clean_list[loop_start]['height'])
        if clean_list[loop_start]['experience'] == "NO":
            clean_list[loop_start]['experience'] = False
        else:
            clean_list[loop_start]['experience'] = True
        clean_list[loop_start]['guardians'] = clean_list[loop_start]['guardians'].split('and')
        loop_start += 1
    #time to pass the cleaned list into a function to create and balance teams
    team_maker(clean_list)

    
def team_maker(clean_list):
    team_PANTHERS = []
    team_BANDITS = []
    team_WARRIORS = []
    exp_players_list = []
    inexp_players_list = []
    #put exp players into a list
    for exp_players in clean_list:
        if exp_players['experience'] == True:
            exp_players_list.append(exp_players)
    sort_end = len(exp_players_list)
    #put inexperienced players into a list
    for inexp_players in clean_list:
        if inexp_players['experience'] == False:
            inexp_players_list.append(inexp_players)
    #distribute the experience players into a team        
    counter = 0
    sort_end = len(inexp_players_list)
    while counter != sort_end:
        team_PANTHERS.append(inexp_players_list[counter])
        counter += 1
        team_BANDITS.append(inexp_players_list[counter])
        counter += 1
        team_WARRIORS.append(inexp_players_list[counter])
        counter += 1
    #distribute the inexperienced players into a team
    counter = 0
    sort_end = len(exp_players_list)
    while counter != sort_end:
        team_PANTHERS.append(exp_players_list[counter])
        counter += 1
        team_BANDITS.append(exp_players_list[counter])
        counter += 1
        team_WARRIORS.append(exp_players_list[counter])
        counter += 1 
    #pass the team along
    team_maker_start(team_PANTHERS, team_BANDITS, team_WARRIORS)

def team_maker_start(team_PANTHERS, team_BANDITS, team_WARRIORS):
    print("Welcome to Cody's Basket Ball Stats Tool")
    start_select = input("Please enter the letter you want to perform\n Enter A for Team Stats \n Enter B to exit \n Enter Here: ")
    if start_select.lower() == "a":
        team_display(team_PANTHERS, team_BANDITS, team_WARRIORS)
    elif start_select.lower() == "b":
        print("Thank you for using this program!")
        exit()
    else:
        print("Not a valid entry. Try again...")
        team_maker_start(team_PANTHERS, team_BANDITS, team_WARRIORS)

def team_display(team_PANTHERS, team_BANDITS, team_WARRIORS):
    print("")
    select_team = input("Please Select a Team from Below: \n A) Panthers \n B) Bandits \n C) Warriors\nEnter: ")
    if select_team.lower() == "a":
        team_name = "Panthers"
        players_on_team(team_PANTHERS, team_name)
    elif select_team.lower() == "b":
        team_name = "Bandits"
        players_on_team(team_BANDITS, team_name)
    elif select_team.lower() == "c":
        team_name = "Warriors"
        players_on_team(team_WARRIORS, team_name)
    else:
        print("")
        print("You did not enter a valid choice!" )
        team_display(team_PANTHERS, team_BANDITS, team_WARRIORS)
    
def players_on_team(*team):
    team_name = team[-1]
    team_players = []
    exp_players = []
    inexp_players = []
    player_guards = []
    team_height = 0
    counter = 0
    counter_end = (len(team[0]))
    
    while counter != counter_end:
        team_players.append(team[0][counter]['name'])
        counter += 1
    counter = 0
    counter_end = (len(team[0]))
    while counter != counter_end:
        team_height += team[0][counter]['height']
        counter += 1
    team_height = int(team_height / counter_end)
    counter = 0
    counter_end = (len(team[0]))
    while counter != counter_end:
        if team[0][counter]['experience'] == True:
            exp_players.append(team[0][counter]['experience'])
        else:
            inexp_players.append(team[0][counter]['experience'])
        counter += 1
    counter = 0
    counter_end = (len(team[0]))    
    while counter != counter_end:
        player_guards.append(team[0][counter]['guardians'])
        counter +=1
    guards = str(player_guards).replace("[","").replace("]","").replace("'","").replace("  ","").replace(" ,",", ")    
    print("")
    print(f"Showing players on Team {team_name}")
    print(*team_players, sep =", ")
    print(f"Total Players are {counter_end}")
    print(f"Average Height is {team_height} inches")
    print("There are:", len(exp_players), "experienced players")
    print("There are:", len(inexp_players), "inexperienced players")
    print(f"The player guardians are::: {guards}")
    print("")
    end_of_stat = input("Enter A to return to menu \nEnter B to exit the program\nEnter:  ")
    while True:
        if end_of_stat.lower() == "a":
            print("")
            team_cleaner()
        elif end_of_stat.lower() == "b":
            print("Thank you for using this program!")
            exit()
        else:
            print("")
            end_of_stat = input("No valid entry. Try again! \n Enter a to return to menu\n Enter B to exit the program \nEnter: ")

if __name__ == "__main__":   
    team_cleaner()    