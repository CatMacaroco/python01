class Plant:
    """Blueprint of plant in garden"""
    def __init__(self, name, height):
        """Inititalize a plant"""
        self.name = name
        self.height = height
        self.kind = "regular"

    def grow(self):
        """Increase the plant's height and print message"""
        self.height += 1
        print(f"{self.name} grew 1cm")
        

class FloweringPlant(Plant):
    """Represents a plant that gives flowers"""
    def __init__(self, name, height, color):
        """Initialize a flower plant"""
        super().__init__(name, height)
        self.color = color
        self.kind = "flowering"


class PrizeFlower(FloweringPlant):
    """Represents a plant that wins prizes"""
    def __init__(self, name, height, color, prize_points):
        """Initialize a Flower plant with prize"""
        super().__init__(name, height, color)
        self.prize_points = prize_points
        self.kind = "prize"


class Garden:
    """Blueprint of a garden with plants"""
    def __init__(self, owner):
        """Initialize garden"""
        self.owner = owner
        self.plants = []
        self.plant_count = 0

    def add_plant(self, plant):
        """Add plant to garden"""
        self.plants = self.plants + [plant]
        self.plant_count = self.plant_count + 1
        print(f"Added {plant.name} to {self.owner}'s garden")
    
    def grow_all(self):
        """grow all plants by 1cm and print status"""
        print("")
        print(f"{self.owner} is helping all plants grow...")
        i = 0
        while i < self.plant_count:
            self.plants[i].grow()
            i += 1
    
    def report(self):
        """Print a report of all plants in the garden"""
        print("")
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        i = 0
        while i < self.plant_count:
            x = self.plants[i]
            if x.kind == "prize":
                print(f"- {x.name}: {x.height}cm, {x.color} flowers (blooming), Prize points: {x.prize_points}")
            elif x.kind == "flowering":
                print(f"- {x.name}: {x.height}cm, {x.color} flowers (blooming)")
            else:
                print(f"- {x.name}: {x.height}cm")
            i += 1


class GardenManager:
    """Manages many gardens and makes calculations"""
    def __init__(self):
        """Initialize a Garden Manager with 0 gardens"""
        self.garden = []
        self.garden_count = 0

    def add_garden(self, garden):
        """Adds garden to be managed"""
        self.garden = self.garden + [garden]
        self.garden_count += 1

    class GardenStats:
        """Makes calculations"""
        @staticmethod
        def count_plant_types(plants, count):
            """Count number of plants per type"""
            regular = 0
            flowering = 0
            prize = 0
            i = 0
            while i < count:
                if plants[i].kind == "prize":
                    prize += 1
                elif plants[i].kind == "flowering":
                    flowering += 1
                else:
                    regular += 1
                i += 1
            return regular, flowering, prize


    @staticmethod
    def validate_height(height):
        """Validate that height is not negative"""
        if height >= 0:
            return True
        else:
            return False


    @classmethod
    def create_garden_network(cls, garden, count):
        """Create a Garden Manager and add gardens"""
        manager = cls()
        i = 0
        while i < count:
            manager.add_garden(garden[i])
            i += 1
        return manager
    
    def garden_scores(self):
        """Calculates scores for each garden based on plant height and prize"""
        scores = {}
        i = 0
        while i < self.garden_count:
            c = self.garden[i]
            score = 0
            j = 0
            while j < c.plant_count:
                score += c.plants[j].height
                if c.plants[j].kind == "prize":
                    score += c.plants[j].prize_points
                j += 1
            scores[c.owner] = score
            i += 1
        return scores


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print("")

alice = Garden("Alice")
bob = Garden("Bob")

alice.add_plant(Plant("Oak Tree", 100))
alice.add_plant(FloweringPlant("Rose", 25, "red"))
alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

alice.grow_all()

alice.report()

manager = GardenManager.create_garden_network([alice, bob], 2)

stats = GardenManager.GardenStats
regular, flowering, prize = stats.count_plant_types(alice.plants, alice.plant_count)

print("")
print(f"Plants added: {alice.plant_count}, Total growth: {alice.plant_count}cm")
print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")
print("")
print(f"Height validation test: {GardenManager.validate_height(10)}")

scores = manager.garden_scores()
print(f"Garden scores - Alice: {scores['Alice']}, Bob: {scores['Bob']}")
print(f"Total gardens managed: {manager.garden_count}")
