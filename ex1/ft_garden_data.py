class Plant:
    """Blueprint of plants in the garden"""
    def __init__(self, name, height, age):
        """Define a plant's name, height and age"""
        self.name = name
        self.height = height
        self.age = age

    def info(self):
        """Display plant's information"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


plant1 = Plant("Tulip", 5, 2)
plant2 = Plant("Rose", 2, 3)
plant3 = Plant("Sunflower", 7, 8)

print("=== Garden Plant Registry ===")
plant1.info()
plant2.info()
plant3.info()
