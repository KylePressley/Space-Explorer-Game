import random

class Planet:
    def __init__(self, climate, resources, water, animals, plants):
        self.climate = climate
        self.resources = resources
        self.water = water
        self.animals = animals
        self.plants = plants

class SolarSystem:
    def __init__(self):
        # Increased average resources and number of planets slightly to help balance the game
        self.planets = [Planet(random.randint(1, 10), random.randint(10, 20), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)) for _ in range(random.randint(6, 12))]
        self.current_planet_index = 0

class Player:
    def __init__(self):
        self.resources = 0
        self.materials = []
        self.health = 100

def generate_solar_system():
    return SolarSystem()

def harvest_resources(player, solar_system):
    current_planet = solar_system.planets[solar_system.current_planet_index]
    print(f"\nHarvesting resources from planet {solar_system.current_planet_index + 1}...")

    # Show current planet's full attributes including updated resources
    print(f"Climate: {current_planet.climate}")
    print(f"Water: {current_planet.water}")
    print(f"Animals: {current_planet.animals}")
    print(f"Plants: {current_planet.plants}")
    print(f"Resources: {current_planet.resources} (Depletes as you harvest)")

    # Check if resources are available to harvest
    if current_planet.resources > 0:
        # Ensure the harvest amount is never higher than the remaining resources
        harvest_amount = random.randint(1, min(5, current_planet.resources))
        player.resources += harvest_amount
        player.materials.append(f"{harvest_amount} of planet {solar_system.current_planet_index + 1} resources")
        current_planet.resources -= harvest_amount  # Deplete the planet's resources
        print(f"Harvested {harvest_amount} resources. Remaining resources: {current_planet.resources}.")
        print(f"Total resources collected: {player.resources}.")
    else:
        print("This planet has no more resources to harvest.")

    # Further reduce the health decrease to make the game easier
    health_decrease = max(1, (10 - current_planet.climate) // 6 + (10 - current_planet.water) // 6 + 
                          (10 - current_planet.animals) // 6 + (10 - current_planet.plants) // 6)
    player.health -= health_decrease
    print(f"Health decreased by {health_decrease}. Current health: {player.health}")

def move_to_next_planet(player, solar_system):
    solar_system.current_planet_index += 1
    # Check if there are more planets to explore
    if solar_system.current_planet_index >= len(solar_system.planets):
        print("No more planets to explore in this solar system.")
        solar_system.current_planet_index = len(solar_system.planets) - 1  # Reset index to the last planet
    else:
        # Decrease health for traveling to another planet
        travel_cost = random.randint(1, 2)
        player.health -= travel_cost
        print(f"\nTraveled to the next planet. Health decreased by {travel_cost}. Current health: {player.health}")
        
        # Automatically harvest resources from the new planet
        harvest_resources(player, solar_system)

def display_inventory(player):
    print("\nInventory:")
    if player.materials:
        for material in player.materials:
            print(f"  {material}")
    else:
        print("  No materials collected yet.")
    print(f"Current Health: {player.health}")
    print(f"Total Resources: {player.resources}")

def play_game():
    # Print the introductory story
    print("""
    A distant hum vibrates through the ship, followed by a jolt that sends you tumbling forward. Your eyes snap open, and you find yourself staring at the blinking red lights of the ship's emergency systems. A quick scan of the console reveals the devastating news: your star jump booster has malfunctioned. You're stranded, light-years from home, in an unknown solar system.

    Your heart pounds in your chest. The thought of being stranded, alone and helpless, sends a shiver down your spine. You glance at the medical scanner, which shows your health levels are critically low. The malfunction has taxed your life support systems, leaving you vulnerable to the harsh conditions of this alien world.

    Your family, back on Earth, is waiting for you. They have no idea where you are or what has happened. You must find a way to jump back at lightspeed, even if it means risking everything. The fate of your mission, and perhaps your life, now rests in your hands.
    """)

    player = Player()
    solar_system = generate_solar_system()

    # Display initial inventory and health
    display_inventory(player)

    while True:
        print("\n1. Harvest resources from the current planet")
        print("2. Move to the next planet (risk of finding nothing)")
        print("3. Check inventory and health")
        choice = input("Choose an action: ")

        if choice == "1":
            harvest_resources(player, solar_system)
        elif choice == "2":
            move_to_next_planet(player, solar_system)
        elif choice == "3":
            display_inventory(player)
        else:
            print("Invalid choice. Please choose a valid option.")

        # Check if player has enough resources to build the engine or if health is depleted
        if player.resources >= 100:
            print("\nCongratulations! You have enough resources to build a lightspeed engine. You engage your hyperdrive thrusters and blast off back to Earth!")
            break
        if player.health <= 0:
            print("\nGame over! Your health has reached zero.")
            break
        if solar_system.current_planet_index == len(solar_system.planets) - 1 and solar_system.planets[solar_system.current_planet_index].resources == 0:
            print("""
            
            Oops! You ran out of planets and resources before building your booster. Turns out, you forgot to check 
            the fuel gauge—just like that time you got stuck on the highway with an empty tank! Now you're drifting 
            in space, wondering how a spaceship doesn't have a "low fuel" light.
            
            """)
            break

def main():
    while True:
        play_game()
        restart = input("\nWould you like to play again? (yes/no): ").lower()
        if restart != 'yes':
            print("Thanks for playing! Safe travels, space explorer.")
            break

if __name__ == "__main__":
    main()

