def get_valid_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number (e.g., 10.50).")

def get_non_empty_string(prompt: str) -> str:
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("❌ This field cannot be left blank. Please try again.")