from random import randrange


class Player:
    status = {}

    def __init__(self):
        self.status["level"] = 1
        self.status["experience"] = 0
        self.status["attack"] = 1
        self.status["num_of_attacks"] = 1

    def get_status(self):
        return self.status

    def add_experience(self, val):
        self.status["experience"] += val
        if self.status["experience"] >= 5:
            self.__level_up()
            self.status["experience"] = 0

    def attack(self, boss):
        attack = self.__calc_attack_val()
        damage = boss.receive_damage(attack)

        return damage

    def __level_up(self):
        self.status["level"] += 1
        self.status["attack"] += 1
        if (self.status["level"] % 2) == 0:
            self.status["num_of_attacks"] += 1
        print("  レベル " + str(self.status["level"]) + " にレベルアップした！")
        print("  現在の攻撃力: " + str(self.status["attack"]))
        print("  現在の攻撃回数: " + str(self.status["num_of_attacks"]))
        print()

        return

    def __calc_attack_val(self):
        random_val = randrange(
            self.status["attack"] - 1, self.status["attack"] + 2)
        attack_val = self.status["attack"] + random_val
        return attack_val
