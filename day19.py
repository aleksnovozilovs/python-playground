class Computer:

    def __init__(self, brand, cpu, ram):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram

    def display_info(self):
        print ()
        print(f"Brand: {self.brand}")
        print(f"CPU: {self.cpu}")   
        print(f"RAM: {self.ram}") 
        print()
    
    def upgrade_ram(self, new_ram):
        self.ram = new_ram
        print()
        
macbook = Computer("Apple", "M4", "24GB")
hp = Computer("HP", "Intel Core i5", "16GB")

macbook.display_info()
hp.display_info()

new_ram = input("Enter new RAM: ")
upgraded_device = input("Which device would you like to upgrade? ").casefold()
if upgraded_device == "macbook":
    macbook.upgrade_ram(new_ram)
elif upgraded_device =="hp":
    hp.upgrade_ram(new_ram)

macbook.display_info()
hp.display_info()




