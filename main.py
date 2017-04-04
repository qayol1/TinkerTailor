class Alogrithm:
    def __init__(self, players, step):
        self.players = players
        self.step = step
        self.index = 0
        self.players_list = []
        self.result = []

    def create_list(self):
        if self.step > self.players:
            self.step = self.step % self.players
            if self.step == 0:
                self.step = 1
        for i in range(1, self.step * (self.step +1)):
            for j in range(1, self.players + 1):
                self.players_list.append(j)

    def store_player_to_eliminate(self, eliminated_player):
        self.result.append(eliminated_player)

    def eliminate_player(self):
        player_to_eliminate = self.players_list[self.index]
        self.store_player_to_eliminate(player_to_eliminate)
        for i, element in enumerate(self.players_list):
            if i > self.index:
                if self.players_list[i] == player_to_eliminate:
                    del self.players_list[i]

    def execute(self):
        self.create_list()
        self.index = self.step - 1
        self.eliminate_player()
        for i in range(self.players - 1):
            self.index += self.step
            self.eliminate_player()


def get_players_number():
    while True:
        try:
            players = int(input("Pleas enter the number of the players: "))
            if int(players) > 1:
                break
            print("Players number must be 2 or greater!")
        except ValueError:
            print("Please enter an integer!")
    return players


def get_step_number():
    while True:
        try:
            step = int(input("Please enter the rhyme's length:"))
            if int(step) > 0:
                break
            print("The length most be 1 or greater!")
        except ValueError:
            print("Please enter an integer!")
    return step


def start_algorithm():
    players = get_players_number()
    step = get_step_number()
    algorithm = Alogrithm(players, step)
    algorithm.execute()
    print(algorithm.result)


def main():
    start_algorithm()


if __name__ == "__main__":
    main()
