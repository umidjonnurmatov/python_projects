import random
import string

def generate_password(length = 12, strong = True):
    if strong:
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    print("Password Generator")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        strong_choice = input("Strong password? (y/n, default y) ").lower() or 'y'
        strong = strong_choice == 'y'
        password = generate_password(length, strong)
        print(f"\nYour generated password is : {password}")
    except ValueError:
        print("Invalid input! Please enter a number for length.")


