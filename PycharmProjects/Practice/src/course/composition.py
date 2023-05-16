# Player class
class Player:
    def __init__(self, playerId, name, teamName):
        self.ID = playerId
        self.name = name
        self.teamName = teamName

    # Complete the implementation


# Team class contains a list of Player
# Objects
class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    # Complete the implementation


# School class contains a list of Team
# objects.
class School:
    def __inti__(self, schoolName):
        self.name = schoolName
        self.teams = []

    def addTeam(self, addTeam):
        self.teams.append(addTeam)

    def getTotalPlayersInSchool(self, team):
        return len(team.players)


player = Player(1, "ned", "NedTeam")
team = Team("NedTeam")

school = School("Legends")
school.addTeam(team.addPlayer(player))

print(school.getTotalPlayersInSchool(team))
