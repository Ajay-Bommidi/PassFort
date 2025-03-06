# 🔐 Advanced Password Strength Checker - PassFort

## 🚀 Introduction
PassFort is an advanced password strength checker designed for security-conscious users. It analyzes password strength using multiple factors, including length, character diversity, common patterns, entropy, and predictability. This tool helps users create and evaluate strong passwords while providing real-time feedback and improvement suggestions.

## 🎯 Features
- **Real-Time Strength Analysis**: Checks password strength based on length, complexity, entropy, and common vulnerabilities.
- **Entropy Calculation**: Provides entropy score (measured in bits) to assess password randomness.
- **Interactive CLI UX**: Uses a sleek command-line interface with color-coded outputs.
- **Secure Input Handling**: Password input is hidden with `•` feedback to prevent shoulder-surfing.
- **Password Visibility Toggle**: Users can choose to reveal their password for verification.
- **Password Suggestions**: Generates highly secure, random passwords.
- **Common Weakness Checks**: Detects common password patterns, repeated characters, and predictable sequences.

## 🛠 Installation
To use PassFort, ensure you have Python installed. Then, clone this repository and install dependencies:

```sh
# Clone the repository
git clone https://github.com/your-username/PassFort.git


# Install required dependencies
pip install -r requirements.txt
```

## 🚀 Usage
Run the script from the terminal:

```sh
python password_checker.py
```

### 📝 How It Works
1. Enter a password (input will be hidden for security).
2. The tool will analyze the password and display:
   - Strength rating (Weak, Moderate, Strong, Unbreakable)
   - Entropy score (measured in bits)
   - Feedback for improving the password (if applicable)
3. Optionally, generate a strong random password.
4. Option to analyze another password or exit.

## 📌 Example Output
```
██████╗  █████╗ ███████╗███████╗███████╗███████╗ ██████╗ ████████╗
██╔══██╗██╔══██╗╚══███╔╝╚══███╔╝██╔════╝██╔════╝██╔═══██╗╚══██╔══╝
██║  ██║███████║  ███╔╝   ███╔╝ █████╗  █████╗  ██║   ██║   ██║   
██║  ██║██╔══██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══╝  ██║   ██║   ██║   
██████╔╝██║  ██║███████╗███████╗███████╗██║     ╚██████╔╝   ██║   
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝      ╚═════╝    ╚═╝   

🔐 Advanced Password Strength Checker 🔐

Enter your password (typing hidden, but active): ********

🔹 Password Strength: 🟢 Unbreakable
🔹 Entropy: 85.6 bits
✔️ Your password is strong and secure!

Do you want a randomly generated strong password? (y/n): y
💡 Suggested Strong Password: X$7k3y@R9v^Pq8*
(Ensure you store it securely!)

Do you want to check another password? (y/n): n
🔐 Stay secure! Exiting PassFort... 👋
```

## 🔧 Customization
- Change password length requirements in `password_checker.py`.
- Adjust entropy thresholds for stricter security policies.
- Modify the `generate_strong_password()` function to customize character sets.

## 💡 Future Enhancements
- **GUI Version** using Tkinter or PyQt.
- **Database Integration** to check against leaked password databases.
- **Online API** for real-time password security analysis.

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repo, create issues, and submit pull requests.

## ⚖️ License
This project is licensed under the MIT License.
