class Computer:

    def __init__(self, brand, cpu, ram):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram

    def display_info(self):
        print()
        print(f"Brand: {self.brand}")
        print(f"CPU: {self.cpu}")
        print(f"RAM: {self.ram}")
        print()

class GamingComputer (Computer):

    def play_game(self):
        print("Launching game.......")
        print()

aleks_laptop = GamingComputer("Alienware", "Intel i9", "32GB")
aleks_laptop.display_info()
aleks_laptop.play_game()
