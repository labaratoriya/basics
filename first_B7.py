# Write a function which inputs the names of two football teams,
# and the score of one team followed by the score of the other team.
# Your function should calculate how many points
# each team gets (3 for a win,1 for a draw, 0 if they lose).

def main():
    team1 = raw_input("Football team 1 'Home': ")
    team2 = raw_input("Football team 2 'Guest': ")
    team1Score = int(raw_input("What is their final score of {0} ".format(team1)))
    team2Score = int(raw_input("What is the final scor of Guest {0} ".format(team2)))

    #print (team1, team2)
    #print (team1Score, team2Score)

    if team1Score > team2Score:
        print("{0} wins and get 3 points, {1} loose and get 0 point".format(team1,team2))
    elif team1Score == team2Score:
        print ("Each teams {0} and {1} get 2 point for a Draw".format(team1,team2))
    elif team1Score < team2Score:
        print("Your {0} team loose and got 0 points, {1} win and get 3 points!".format(team1,team2))
# it still have no "else" on the end
