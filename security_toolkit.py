
MIN_LENGTH = 8
def border(width):
    """Print a border."""
    print("+" + "-" * width + "+")

def show_box(text):
    """Display text inside a box."""
    width = len(text) + 2
    border(width)
    print("| " + text + " |")
    border(width)


def show_menu():
    """Display the menu."""
    print("SECURITY TOOLKIT")
    print("1. Check a port")
    print("2. Check a password")
    print("3. PIN guessing time")
    print("q. Quit")
def port_range(port):
    """Identify the port range."""
    if 0 <= port <= 1023:
        return "system"
    elif 1024 <= port <= 49151:
        return "user"
    elif 49152 <= port <= 65535:
        return "dynamic"
    else:
        return "invalid"


def check_port():
    """Check a port."""
    port = int(input("Port: "))
    result = port_range(port)
    show_box(f"Port {port}: {result}")


def password_problem(password, username):
    """Check password requirements."""
    if password == username:
        return "Rejected: same as the username"
    elif len(password) < MIN_LENGTH:
        return "Rejected: too short"
    else:
        return "Password accepted"


def check_password():
    """Check a username and password."""
    username = input("Username: ")
    password = input("Password: ")

    result = password_problem(password, username)
    show_box(result)


def days_to_guess(digits, per_second):
    """Calculate PIN guessing time in days."""
    total_guesses = 10 ** digits
    seconds = total_guesses / per_second
    days = int(seconds / 86400)

    return days


def check_pin():
    """Calculate PIN guessing time."""
    digits = int(input("PIN digits: "))
    per_second = int(input("Guesses per second: "))

    days = days_to_guess(digits, per_second)
    show_box(f"{digits} digits: {days} days")

show_menu()

checks = 0

while True:

    choice = input("Choice (1, 2, 3, or q): ")

    if choice == "1":
        check_port()
        checks += 1

    elif choice == "2":
        check_password()
        checks += 1

    elif choice == "3":
        check_pin()
        checks += 1

    elif choice == "q":
        show_box(f"Checks done: {checks}")
        break

    else:
        print("Unknown choice.")