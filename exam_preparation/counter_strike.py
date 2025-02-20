class BattleGame:
    def __init__(self, energy):
        self.energy = energy
        self.won_battles = 0

    def play(self):
        command = input()
        while command != "End of battle":
            distance = int(command)
            if self.energy >= distance:
                self.energy -= distance
                self.won_battles += 1
                if self.won_battles % 3 == 0:
                    self.energy += self.won_battles

                command = input()
            else:
                return f"Not enough energy! Game ends with {self.won_battles} won battles and {self.energy} energy"
        else:
            return f"Won battles: {self.won_battles}. Energy left: {self.energy}"


energy = int(input())
game = BattleGame(energy)
result = game.play()
print(game)
