class LifeSimulator:
    def __init__(self):
        self.health = 100
        self.career = 50
        self.happiness = 50

    def make_decision(self, decision):
        if decision == "work_hard":
            self.career += 10
            self.health -= 5
        elif decision == "relax":
            self.happiness += 10
        elif decision == "exercise":
            self.health += 10

    def status(self):
        return {
            "Health": self.health,
            "Career": self.career,
            "Happiness": self.happiness
        }


if __name__ == "__main__":
    sim = LifeSimulator()
    sim.make_decision("work_hard")
    print(sim.status())
