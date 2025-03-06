import re
import string
import math
import secrets
import sys
import time
import getpass
from colorama import Fore, Style, init

# Initialize Colorama for colored CLI output
init(autoreset=True)

# ASCII Banner
def banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
______             ______         _   
| ___ \            |  ___|       | |  
| |_/ /_ _ ___ ___ | |_ ___  _ __| |_ 
|  __/ _` / __/ __||  _/ _ \| '__| __|
| | | (_| \__ \__ \| || (_) | |  | |_ 
\_|  \__,_|___/___/\_| \___/|_|   \__|
""" + Fore.YELLOW + Style.BRIGHT + """
               🔐 PassFort - Advanced Password Checker
               Author: Ajay Bommidi
""" + Style.RESET_ALL)

banner()

def entropy(password):
    """Calculate password entropy (bits of randomness)."""
    character_set_size = 0
    if any(c.islower() for c in password):
        character_set_size += 26
    if any(c.isupper() for c in password):
        character_set_size += 26
    if any(c.isdigit() for c in password):
        character_set_size += 10
    if any(c in string.punctuation for c in password):
        character_set_size += len(string.punctuation)
    
    if character_set_size == 0:
        return 0
    
    return round(len(password) * math.log2(character_set_size), 2)

def generate_strong_password(length=16):
    """Generate a strong random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def check_password_strength(password):
    """Assess the strength of a password."""
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append(Fore.RED + "❌ Password is too short! Use at least 12 characters.")
    
    # Upper and lowercase check
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 2
    else:
        feedback.append(Fore.YELLOW + "⚠️ Mix uppercase and lowercase letters for better security.")
    
    # Number check
    if re.search(r"\d", password):
        score += 2
    else:
        feedback.append(Fore.YELLOW + "⚠️ Add numbers to increase password strength.")
    
    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        feedback.append(Fore.YELLOW + "⚠️ Include special characters (e.g., @, #, $) to enhance security.")
    
    # Common pattern check
    common_patterns = ["password", "123456", "qwerty", "admin", "letmein", "welcome"]
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append(Fore.RED + "❌ Avoid common words or predictable sequences in your password.")
        score -= 2
    
    # Repetitive characters check
    if re.search(r"(.)\1{2,}", password):
        feedback.append(Fore.YELLOW + "⚠️ Avoid repeated characters (e.g., aaa, 111).")
        score -= 1
    
    # Sequential characters check
    if re.search(r"123|abc|qwerty", password.lower()):
        feedback.append(Fore.RED + "❌ Avoid sequential characters (e.g., 1234, abcd, qwerty).")
        score -= 2
    
    # Entropy calculation
    entropy_bits = entropy(password)
    if entropy_bits < 50:
        feedback.append(Fore.RED + f"❌ Weak password entropy: {entropy_bits} bits. Aim for 70+ bits.")
    
    # Password Strength Levels
    if score >= 8:
        strength = Fore.GREEN + "🟢 Unbreakable"
    elif score >= 6:
        strength = Fore.BLUE + "🔵 Strong"
    elif score >= 4:
        strength = Fore.YELLOW + "🟡 Moderate"
    else:
        strength = Fore.RED + "🔴 Weak"
    
    return strength, feedback, entropy_bits

def type_effect(text, delay=0.05):
    """Typewriter effect for better UX."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_password():
    """Secure password input with dot feedback."""
    password = ""
    while True:
        char = getpass.getpass(Fore.BLUE + "Enter your password (typing hidden, but active): ")
        if char:
            password = char
            break
        else:
            print(Fore.RED + "⚠️ Please enter a valid password!")
    return password

def main():
    print(Fore.CYAN + "\n🔒 Advanced Password Strength Checker 🔒\n")
    
    while True:
        password = get_password()
        
        # Option to reveal password
        show_password = input(Fore.CYAN + "Do you want to reveal the password? (y/n): ").strip().lower()
        if show_password == 'y':
            print(Fore.MAGENTA + f"Your password: {password}")

        # Analyze password strength
        strength, feedback, entropy_bits = check_password_strength(password)
        
        # Display results with typewriter effect
        type_effect(f"\n🔹 Password Strength: {strength}", 0.03)
        type_effect(f"🔹 Entropy: {entropy_bits} bits", 0.03)
        
        if feedback:
            print(Fore.YELLOW + "\nSuggestions to Improve Your Password:")
            for msg in feedback:
                type_effect(msg, 0.02)
        else:
            print(Fore.GREEN + "✔️ Your password is strong and secure!")
        
        # Generate a strong password if requested
        generate_new = input(Fore.CYAN + "\nDo you want a randomly generated strong password? (y/n): ").strip().lower()
        if generate_new == 'y':
            new_password = generate_strong_password()
            print(Fore.GREEN + f"💡 Suggested Strong Password: {new_password}")
            print(Fore.YELLOW + "(Ensure you store it securely!)")
        
        # Check another password or exit
        another = input(Fore.CYAN + "\nDo you want to check another password? (y/n): ").strip().lower()
        if another != 'y':
            print(Fore.GREEN + "\n🔐 Stay secure! Exiting PassFort... 👋")
            break

if __name__ == "__main__":
    main()
