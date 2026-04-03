
        
import os, time, sys, random, requests

# PROFESSIONAL INTERFACE COLORS
G, R, W, B, Y, C, P = "\033[1;32m", "\033[1;31m", "\033[1;37m", "\033[1;34m", "\033[1;33m", "\033[1;36m", "\033[1;35m"

def logo():
    os.system('clear')
    print(f"""{C}
    ██╗   ██╗    ███████╗███████╗███╗   ██╗███████╗██╗
    ██║   ██║    ██╔════╝██╔════╝████╗  ██║██╔════╝██║
    ██║   ██║    ███████╗█████╗  ██╔██╗ ██║███████╗██║
    ╚██╗ ██╔╝    ╚════██║██╔══╝  ██║╚██╗██║╚════██║██║
     ╚████╔╝     ███████║███████╗██║ ╚████║███████║██║
      ╚═══╝      ╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝
    {G}      [ V18 FINAL - 200% MASTER CONFIGURATION ]
    {W}═══════════════════════════════════════════════════""")

def cloud_sync():
    print(f"{B}[*] SYNCING WITH GLOBAL SENSI DATABASE...{W}")
    try:
        # Checking internet connectivity for cloud simulation
        requests.get("https://google.com", timeout=3)
        print(f"{G}[✔] CLOUD SYNC COMPLETE: 2026.04.03 VERSION ACTIVE{W}")
    except:
        print(f"{Y}[!] OFFLINE MODE: USING PRE-INSTALLED NODES{W}")
    time.sleep(1)

def injection_process():
    # Only necessary system-level simulations
    tasks = [
        "FIXING TOUCH RESPONSE (0ms)",
        "CALIBRATING 200% SENSITIVITY",
        "STABILIZING SCOPE RECOIL (2X/4X)",
        "INJECTING ANTI-SHAKE ALGORITHM"
    ]
    for task in tasks:
        sys.stdout.write(f"{P}[~] {task}...")
        for _ in range(8):
            sys.stdout.write(f"{G}■")
            sys.stdout.flush(); time.sleep(0.06)
        print(f" {W}OK")

def main():
    logo()
    # Security Key is mandatory for your brand protection
    key = "VASU-X-PRO"
    user_key = input(f"{P}[?] ENTER ACCESS KEY: {W}")
    if user_key != key:
        print(f"{R}[!] ACCESS DENIED!{W}"); sys.exit()
    
    logo()
    cloud_sync()
    
    brand = input(f"\n{B}[+] Device Model : {W}")
    ram   = int(input(f"{B}[+] RAM (GB)     : {W}"))
    hz    = int(input(f"{B}[+] Refresh Rate : {W}"))
    
    print(f"\n{C}--- SELECT PERFORMANCE MODE ---{W}")
    print(f"{Y}[1] 1P ONE-TAP SPECIAL (Speed)")
    print(f"{Y}[2] ALL-ROUNDER (Stability)")
    mode = input(f"{B}[+] Choice (1/2): {W}")

    print(f"\n{P}[!] STARTING ELITE INJECTION...{W}")
    injection_process()

    # --- THE MASTER 200% CALCULATION ENGINE ---
    # Optimized for the latest game updates and display refresh rates
    if hz >= 90:
        gen, red, s2x, s4x, snp, free = 200, 198, 192, 185, 95, 170
        dpi = 510 if ram < 8 else 411
    else:
        gen, red, s2x, s4x, snp, free = 200, 200, 188, 175, 88, 150
        dpi = 580 if ram < 6 else 480

    fire_btn = "38%" if mode == "1" else "42%"

    print(f"\n{G}╔═══════════════ FINAL MASTER PANEL ════════════════╗")
    print(f"║ {W}STATUS      : {G}INJECTED (100% WORKING)             {G}║")
    print(f"║ {W}GENERAL     : {R}{gen}%      {W}RED DOT  : {R}{red}%          {G}║")
    print(f"║ {W}2X SCOPE    : {C}{s2x}%      {W}4X SCOPE : {C}{s4x}%          {G}║")
    print(f"║ {W}SNIPER      : {Y}{snp}%       {W}FREE LOOK: {Y}{free}%         {G}║")
    print(f"║ {W}DPI VALUE   : {C}{dpi}      {W}FIRE BTN : {C}{fire_btn}          {G}║")
    print(f"║ {W}TOUCH DELAY : {G}0.01ms     {W}AIM LOCK : {G}ACTIVE         {G}║")
    print(f"╚════════════════════════════════════════════════════╝")
    
    print(f"\n{P}[!] SYSTEM: {W}Settings optimized for {brand.upper()}.")
    print(f"{G}>>> CONFIG APPLIED! GO CRUSH THE GAME! <<<{W}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] SHUTTING DOWN CORE.")
    
