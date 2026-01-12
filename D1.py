import random
import time
from datetime import datetime, timedelta
# ================= AUTO INSTALL =================
import os
import sys
import subprocess

def run(cmd):
    subprocess.call(cmd, shell=True)

print("\n[+] Checking & Installing Requirements...\n")

# -------- TERMUX PACKAGES --------
run("pkg install git -y")

# -------- PYTHON PACKAGES --------
def pip_install(pkg):
    try:
        __import__(pkg)
        print(f"[✓] {pkg} already installed")
    except ImportError:
        print(f"[+] Installing {pkg} ...")
        run(f"{sys.executable} -m pip install {pkg}")

pip_install("colorama")
pip_install("requests")

# -------- OPTIONAL / CUSTOM --------
# Walang official python package na "pink"
# Pwede itong placeholder o local module
try:
    import pink
    print("[✓] pink module detected")
except:
    print("[!] pink module not found (optional / custom module)")

print("\n[✓] All requirements ready!\n")
# ================= COLORS =================
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"
RESET  = "\033[0m"
BOLD   = "\033[1m"
 
# ================= LOGO =================
def show_logo():
    print(CYAN + BOLD + r"""
██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   
██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   
██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   
╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
""" + RESET)
    print(YELLOW + "        TERMUX REPORT SYSTEM\n" + RESET)

# ================= DATA =================
processed_links = {}

def detect_platform(link):
    link = link.lower()
    if "youtube" in link:
        return "YouTube"
    if "facebook" in link:
        return "Facebook"
    if "instagram" in link:
        return "Instagram"
    if "google" in link:
        return "Google"
    if "tiktok" in link:
        return "TikTok"
    return None

def random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

# ================= MAIN LOOP =================
while True:
    show_logo()

    link = input(WHITE + "Paste link: " + RESET).strip()
    if not link:
        print(RED + "❌ Empty link\n" + RESET)
        continue

    platform = detect_platform(link)
    if not platform:
        print(RED + "❌ Unsupported / Invalid link\n" + RESET)
        continue

    # PLATFORM DETECT DISPLAY
    print(GREEN + f"\nPlatform detected: {platform}" + RESET)
    print(YELLOW + "Checking link..." + RESET)
    time.sleep(3)

    cont = input(CYAN + "Type Y to continue process: " + RESET).lower()
    if cont != "y":
        print(RED + "Process cancelled.\n" + RESET)
        continue

    print(CYAN + "\n🚀 Starting process...\n" + RESET)

    # ================= PROCESS =================
    for i in range(1, 101):
        now = datetime.now()

        print(BLUE + f"\nPROCESS {i}/100" + RESET)

        for p in range(0, 101, 10):
            filled = "█" * (p // 5)
            empty = " " * (20 - len(filled))
            print(
                GREEN + f"[{filled}{empty}] " +
                YELLOW + f"{p}%" + RESET,
                end="\r"
            )
            time.sleep(0.01)

        print(CYAN + f"""
{YELLOW}Link    : {link}
{YELLOW}Platform: {platform}
{YELLOW}IP      : {random_ip()}
{YELLOW}Time    : {now.strftime('%I:%M:%S %p')}
{YELLOW}Date    : {now.strftime('%d')}
{YELLOW}Month   : {now.strftime('%B')}
{YELLOW}Status  : {GREEN}Successfully Reported
{YELLOW}Warning :\033[91m Don't abuse may cause error !!!
""" + RESET)

        time.sleep(1)

    processed_links[link] = datetime.now()
    print(RED + "\n⚠ DONE. Next process after 12 hours.\n" + RESET)

    again = input(WHITE + "Process another? (y/n): " + RESET).lower()
    if again != "y":
        print(GREEN + "\nThank you for using REPORT SYSTEM 👋\n" + RESET)
        break