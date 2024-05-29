import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} на {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        turn = 0  # 0 for player, 1 for computer
        while self.player.is_alive() and self.computer.is_alive():
            if turn == 0:
                self.player.attack(self.computer)
                print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")
                turn = 1
            else:
                self.computer.attack(self.player)
                print(f"У {self.player.name} осталось {self.player.health} здоровья.")
                turn = 0

            # Добавим паузу между ходами для удобства чтения
            input("Нажмите Enter для следующего хода...")

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    computer_name = "Компьютер"

    game = Game(player_name, computer_name)
    game.start()