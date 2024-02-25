from .character import *


def run():
    print("---- Charaquest Start ----")
    characters = character_init()

    while characters["boss"].get_hp_status() > 0:
        print("ボスの残り HP: " + str(characters["boss"].get_hp_status()))
        input()

        for i in range(characters["player"].get_status()["num_of_attacks"]):
            damage = characters["player"].attack(characters["boss"])
            print("ボス1に " + str(damage) + " のダメージを与えた！")

        damage = characters["player"].add_experience(1)

    print()
    print("★★★★★★★★★★★★★★★")
    print("ボスを倒した！おめでとう！")
    print("★★★★★★★★★★★★★★★")
    print()
