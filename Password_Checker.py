import re
import hashlib
import sqlite3

# -------------------------------
# Common Password Check
# -------------------------------

def load_common_passwords():
    try:
        with open("common_passwords.txt", "r") as f:
            return set(password.strip() for password in f.readlines())
    except FileNotFoundError:
        return set()

common_passwords = load_common_passwords()

# -------------------------------
# Password Strength Checker
# -------------------------------

def check_password_strength(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # Common Password Check
    if password.lower() in common_passwords:
        feedback.append("This is a commonly used password.")
        score = 0

    # Strength Rating
    if score <= 2:
        strength = "Weak"
    elif score <= 5:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback

# -------------------------------
# Suggest Strong Password
# -------------------------------

def suggest_password(password):
    suggestion = password

    if len(suggestion) < 12:
        suggestion += "X9!"

    if not re.search(r"[A-Z]", suggestion):
        suggestion += "A"

    if not re.search(r"[a-z]", suggestion):
        suggestion += "a"

    if not re.search(r"\d", suggestion):
        suggestion += "7"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", suggestion):
        suggestion += "@"

    return suggestion

# -------------------------------
# Optional Password History
# -------------------------------

conn = sqlite3.connect("password_history.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS passwords(
hash TEXT UNIQUE
)
""")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def password_used_before(password):
    hashed = hash_password(password)
    cursor.execute("SELECT * FROM passwords WHERE hash=?", (hashed,))
    return cursor.fetchone() is not None

def save_password(password):
    hashed = hash_password(password)
    try:
        cursor.execute("INSERT INTO passwords(hash) VALUES(?)", (hashed,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass

# -------------------------------
# Main Program
# -------------------------------

password = input("Enter Password: ")

if password_used_before(password):
    print("\nWarning: Password has been used before.\n")

strength, feedback = check_password_strength(password)

print("\nPassword Strength:", strength)

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)

if strength != "Strong":
    print("\nSuggested Password:")
    print(suggest_password(password))

save_password(password)

conn.close()