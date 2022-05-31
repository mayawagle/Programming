class Baseball_Player:
    def __init__(self):
        self.team = 'Team'
        self.name = 'Name'
        self.height = 'Height'
    def __init__(self, team):
        self.team = team
        self.name = 'Name'
        self.height = 'Height'

players1 = Baseball_Player()
player2 = Baseball_Player("ari's awesome players", )
print(players1)
print(players1.height)