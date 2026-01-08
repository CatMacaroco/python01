class Plant:
    """Blueprint of plants (name, height and age) in the garden"""
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


plant1 = Plant("Tulip", 5, 2)
plant2 = Plant("Rose", 2, 3)
plant3 = Plant("Sunflower", 7, 8)

print("=== Garden Plant Registry ===")
plant1.display()
plant2.display()
plant3.display()
