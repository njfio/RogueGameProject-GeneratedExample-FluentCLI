def get_user_input(prompt, valid_choices):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_choices:
            return user_input
        else:
            print("Invalid input. Please try again.")

def validate_integer_input(prompt, min_value, max_value):
    while True:
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("Welcome to the Rogue-like Game!")

    # Example usage of user validation prompts
    name = input("Enter your character name: ")
    while len(name) < 3 or len(name) > 15:
        print("Character name must be between 3 and 15 characters.")
        name = input("Enter your character name: ")

    race = get_user_input("Choose your race (human/elf/dwarf): ", ["human", "elf", "dwarf"])

    class_choice = get_user_input("Choose your class (warrior/mage/rogue): ", ["warrior", "mage", "rogue"])

    age = validate_integer_input("Enter your character's age (18-100): ", 18, 100)

    # Display the character information
    print("\nCharacter Information:")
    print(f"Name: {name}")
    print(f"Race: {race.capitalize()}")
    print(f"Class: {class_choice.capitalize()}")
    print(f"Age: {age}")

if __name__ == "__main__":
    main()
