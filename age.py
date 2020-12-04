#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in December 2020
# Age range


def main():
    # This function checks if the user is in the proper age range

    print("Grandma: I will only let you date my grandchild"
          "if you are between the age of 25 and 40!")

    # Input
    age_string = input("Enter your age: ")

    # Process
    try:
        age = int(age_string)

        if age > 25 and age < 40:
            print("You are the right age! You can date my grandchild!")
        else:
            print("You are not the right age! You cannot date my grandchild!")

    except Exception:
        print("This isn't a valid age")


if __name__ == "__main__":
    main()
