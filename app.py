import os

def greet_user(username):
    print(f"Hello, {username}!")

def main():
    username = os.getenv("USER_NAME", "Guest")
    greet_user(username)  # Fix: Call the greet_user function
    print("Program executed successfully.")

if __name__ == "__main__":
    main()
