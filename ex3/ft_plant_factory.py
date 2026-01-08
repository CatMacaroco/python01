class Plant:
    """Blueprint of plants in a garden"""
    def __init__(self, name, height, age):
        """Define a plant's name, height and age"""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        """Display plant's information"""
        print(f"{self.name} ({self.height}cm, {self.age} days)")


print("=== Plant Factory Output ===")

plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Oak", 200, 365)
plant3 = Plant("Cactus", 5, 90)
plant4 = Plant("Sunflower", 80, 45)
plant5 = Plant("Fern", 15, 120)

print("Created: ", end="")
plant1.get_info()

print("Created: ", end="")
plant2.get_info()

print("Created: ", end="")
plant3.get_info()

print("Created: ", end="")
plant4.get_info()

print("Created: ", end="")
plant5.get_info()

print("Total plants created: 5")
