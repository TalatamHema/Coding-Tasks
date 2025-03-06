def print_gender(gender):
    switch = {
        'M': "Male",
        'F': "Female"
    }
    print(switch.get(gender.upper(), "Invalid input"))  # Handles lowercase input too

# Example usage:
gender = input("Enter gender (M/F): ")
print_gender(gender)
