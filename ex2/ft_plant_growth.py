class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def growth(self):
        self.height += 6

    def plant_age(self):
        self.age += 6

    def info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


tulip = Plant("Tulip", 5, 2)

print("=== Day 1 ===")
tulip.info()

tulip.growth()
tulip.plant_age()

print("=== Day 7 ===")
tulip.info()
print("Growth this week: +6cm")
