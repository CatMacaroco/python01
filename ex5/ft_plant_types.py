class Plant:
    """Blueprint of plants in a garden"""
    def __init__(self, name, height, age):
        """Define a plant's name, height and age"""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Plant (parent) attributes plus flower's"""
    def __init__(self, name, height, age, color):
        """Plant attributes plus flower's"""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Define flower's bloom"""
        print(self.name, "is blooming beautifully")


class Tree(Plant):
    """Plant (parent) attributes plus tree's"""
    def __init__(self, name, height, age, trunk_diameter, shade_area):
        """Plant attributes plus tree's"""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_area = shade_area

    def produce_shade(self):
        """Define tree's shade"""
        print(f"{self.name} provides {self.shade_area} square meters of shade")


class Vegetable(Plant):
    """Plant (parent) attributes plus vegetable's"""
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """Plant attributes plus vegetable's"""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


rose = Flower("Rose", 25, 30, "red")
tulip = Flower("Tulip", 35, 1, "yellow")

oak = Tree("Oak", 500, 1825, 50, 78)
palm = Tree("Palm", 120, 50, 30, 2)

tomato = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C")
lettuce = Vegetable("Lettuce", 30, 60, "summer harvest", "iron")


print("=== Garden Plant Types ===")
print("")
print(f"{rose.name} (Flower): {rose.height}cm, {rose.age} days, "
      f"{rose.color} color")
rose.bloom()
print("")
print(f"{oak.name} (Tree): {oak.height}cm, {oak.age} days, "
      f"{oak.trunk_diameter}cm diameter")
oak.produce_shade()
print("")
print(f"{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} "
      f"days, {tomato.harvest_season}")
print(f"{tomato.name} is rich in {tomato.nutritional_value}")
