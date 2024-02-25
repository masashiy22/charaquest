class Boss:
    status = {}

    def __init__(self):
        self.status["hp"] = 200
        self.status["defence"] = 1

    def get_hp_status(self):
        return self.status["hp"]

    def receive_damage(self, attack_val):
        damage = attack_val - self.status["defence"]
        hp_after_damage = self.get_hp_status() - damage
        self.status["hp"] = hp_after_damage

        return damage
