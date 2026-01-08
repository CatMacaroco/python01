class Plant:
    """Blueprint of plants in a garden"""
    def __init__(self, name, height, age):
        """Define a plant's name, height and age"""
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """Grow the plant's height"""
        self.height += 1

    def plant_age(self):
        """Increase the plant's age"""
        self.age += 1

    def get_info(self):
        """Display plant's information"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


rose = Plant("Rose", 25, 30)

print("=== Day 1 ===")
rose.get_info()

rose.grow()
rose.plant_age()

rose.grow()
rose.plant_age()

rose.grow()
rose.plant_age()

rose.grow()
rose.plant_age()

rose.grow()
rose.plant_age()

rose.grow()
rose.plant_age()

print("=== Day 7 ===")
rose.get_info()
growth = rose.height - 25
print(f"Growth this week: +{growth}cm")
