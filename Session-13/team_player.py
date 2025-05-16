class Team:

    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)

    def player_list(self):
        return self.players


class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def play(self):
        return f"{self.name} plays {self.position}"


def main():
    team = Team("Bower Birds")
    team_no_players = Team("Perth Bears")

    player_1 = Player("Jack", "Fullback")
    player_2 = Player("Isaac", "Striker")
    player_3 = Player("Yanna", "Goalkeeper")
    player_4 = Player("Lisa", "Midfield")

    team.add_player(player_2)
    team.add_player(player_1)
    team.add_player(player_4)
    team.add_player(player_3)

    print(f"{team.name} has {len(team.player_list())} players")
    for player in team.player_list():
        print(player.play())

    print()

    print(f"{team_no_players.name} has {len(team_no_players.player_list())} players")
    for player in team_no_players.player_list():
        print(player.play())


if __name__ == "__main__":
    main()
