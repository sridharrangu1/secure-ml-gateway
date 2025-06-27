# token_gen.py

from app.auth import create_token

if __name__ == "__main__":
    token = create_token("user123", "admin")
    print("Your x-token:\n")
    print(token)
