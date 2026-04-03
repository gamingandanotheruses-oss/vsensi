import os, time, sys

def logo():
    os.system('clear')
    print("\033[1;36m╔════════════════════════════════════════════╗")
    print("\033[1;37m║      V-SENSI GOD MODE V6.0 OFFICIAL      ║")
    print("\033[1;36m╚════════════════════════════════════════════╝\033[0m")

logo()
brand = input("Device Brand: ")
ram = int(input("RAM (GB): "))
hz = int(input("Refresh Rate (Hz): "))

print("\n\033[1;32m[*] CALIBRATING SENSITIVITY...\033[0m")
time.sleep(2)

# Logic for different devices
g = 100 if hz < 90 else 94
print(f"\n\033[1;33m>>> BEST SENSI FOR {brand.upper()}:")
print(f"GENERAL: {g} | RED DOT: {g-4}\033[0m\n")

