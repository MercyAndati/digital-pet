class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, min(10, self.hunger - 3))
        self.happiness = max(0, min(10, self.happiness + 1)) 
        print(f"{self.name} is eating. 🍴🥗😊")

    def sleep(self):
        self.energy = max(0, min(10, self.energy + 5))
        print(f"{self.name} is sleeping. 😴")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play!")
            return
            
        self.energy = max(0, min(10, self.energy - 2))
        self.happiness = max(0, min(10, self.happiness + 2)) 
        self.hunger = max(0, min(10, self.hunger + 1))
        print(f"{self.name} is playing. 🐾")

    def train(self, trick=None):
        if trick is None:
            trick = input("Enter a trick to train your pet: ")
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")
        self.energy = max(0, min(10, self.energy - 1)) 
        self.happiness = max(0, min(10, self.happiness + 1))  

    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet.")
        else:
            print(f"{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")

    def get_status(self):
        print(f"\nPet Name: {self.name}")
        print(f"Hunger level: {self.hunger}/10")
        print(f"Energy level: {self.energy}/10")
        print(f"Happiness level: {self.happiness}/10")
        if self.tricks:
            print(f"Tricks learned: {', '.join(self.tricks)}")

    def menu(self):
        while True:
            print("\nPick what action you would like to do (1-7):")
            print("1. Eat")
            print("2. Sleep")   
            print("3. Play")
            print("4. Train")
            print("5. Show Tricks")
            print("6. Get Status")
            print("7. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.eat()
            elif choice == "2":
                self.sleep()
            elif choice == "3":
                self.play()
            elif choice == "4":
                self.train()
            elif choice == "5":
                self.show_tricks()
            elif choice == "6":
                self.get_status()
            elif choice == "7":
                print("Goodbye!")
                exit()
            else:
                print("Invalid choice. Please try again.")

def main():
    print("WELCOME TO THE DIGITAL PET SYSTEM")
    name = input("Enter your pet's name: ")
    pet = Pet(name)
    pet.menu() 

if __name__ == "__main__":
    main()