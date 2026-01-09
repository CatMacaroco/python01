         
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")
        

class FloweringPlant(Plant):
    def __init__(self, name, height=0, color="unknown"):
        super().__init__(name, height)
        self.color = color
        self.blooming = False
    
    def bloom(self):
        self.blooming = True
        print(f"{self.name} is blooming beautifully!")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height=0, color="unknown", prize_points=0):
        super().__init__(name, height, color)
        self.prize_points = prize_points


class GardenManager:
    class GardenStats:

        @staticmethod
        def total_growth(Plant):
            return sum(p.height for p in plants)
        
        def create_garden_network()

        def create_garden_network()
    
def add_plant(self, plant):
    self.plants.append(plant)
    print(f"Added {plant.name} to {self.owner_name}'s garden")

oak = Plant("Oak", 100)
oak.add_plant()

rose = Plant("Rose", 25)
rose.add_plant()

sunflower = Plant("Sunflower", 50)
sunflower.add_plant()


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")



print("Plants in garden:")
print("")
print("")
