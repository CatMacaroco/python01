class SecurePlant:
    """Blueprint of plants in a garden protected from invalid changes"""
    def __init__(self, name, height, age) -> None:
        """Define a plant's name, height and age with valid values"""
        self.__name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.__name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height):
        """Update height if valid"""
        if height >= 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age):
        """Update age if valid"""
        if age >= 0:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self):
        """Print current height"""
        print(f"Height: {self.__height}cm")

    def get_age(self):
        """Print current height"""
        print(f"Age: {self.__age} days")

    def get_name(self):
        """Print plant's name"""
        print(f"Name: {self.__name}")

    def info(self):
        """Print current plant info"""
        print(f"Current plant: {self.__name} "
              f"({self.__height}cm, {self.__age} days)")


print("=== Garden Security System ===")

plant = SecurePlant("Rose", 25, 30)
print("")
plant.set_height(-5)
print("")
plant.info()
