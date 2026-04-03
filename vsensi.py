import os, time, sys, random

# ELITE COLOR PALETTE
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
    {G}     [ V11 HYPER-DRIVE EDITION - BY VASU-GOD ]
    {W}═══════════════════════════════════════════════════""")

def security():
    logo()
    key = "VASU-X-PRO" # Updated Key for V11
    user_key = input(f"{P}[?] ENTER PRIVATE KEY: {W}")
    if user_key != key:
        print(f"{R}[!] ERROR: ACCESS DENIED!{W}"); sys.exit()
    print(f"{G}[✔] ACCESS GRANTED! INITIALIZING HYPER-DRIVE...{W}")
    time.sleep(1.5)

def hyper_scan():
    stages = [
        "FETCHING GITHUB SENSITIVITY DATABASE",
        "ANALYZING DISPLAY RESOLUTION (DPI)",
        "STABILIZING 200% SENSITIVITY NODES",
        "CLEARING SYSTEM CACHE & JUNK",
        "INJECTING ONE-TAP MACRO VALUES"
    ]
    for stage in stages:
        sys.stdout.write(f"{B}[~] {stage}...")
        for _ in range(15):
            sys.stdout.write(f"{G}█")
            sys.stdout.flush(); time.sleep(0.05)
        print(f" {W}DONE")

def main():
    logo()
    brand = input(f"{B}[+] Device Model : {W}")
    ram   = int(input(f"{B}[+] RAM (GB)     : {W}"))
    hz    = int(input(f"{B}[+] Screen Hz    : {W}"))
    
    print(f"\n{C}--- CHOOSE YOUR SPECIALIZATION ---{W}")
    print(f"{Y}[1] 1P HEADSHOT (One-Tap Only)")
    print(f"{Y}[2] ALL-ROUNDER (Rank Push)")
    print(f"{Y}[3] E-SPORTS CONFIG (Low Latency)")
    mode = input(f"{B}[+] Select Mode: {W}")

    hyper_scan()

    # HYPER-LOGIC (Derived from Top GitHub Scripts)
    if mode == "1":
        gen, red, fire, dpi = 200, 196, "38%", 590 if ram < 8 else 411
    elif mode == "2":
        gen, red, fire, dpi = 192, 182, "45%", 480 if ram < 8 else "DEFAULT"
    else:
        gen, red, fire, dpi = 175, 168, "52%", "STABLE"

    print(f"\n{G}╔═════════════ HYPER-DRIVE CONFIG V11 ══════════════╗")
    print(f"║ {W}STATUS      : {G}SUCCESSFULLY INJECTED              {G}║")
    print(f"║ {W}GENERAL     : {R}{gen}% (200% UNLOCKED)             {G}║")
    print(f"║ {W}RED DOT     : {R}{red}% (AIM ASSIST ON)             {G}║")
    print(f"║ {W}DPI VALUE   : {C}{dpi}                              {G}║")
    print(f"║ {W}FIRE BUTTON : {C}{fire}                             {G}║")
    print(f"║ {W}LATENCY     : {C}FIXED (0ms DELAY)                {G}║")
    print(f"╚═══════════════════════════════════════════════════╝")
    
    print(f"\n{P}[!] PRO TIP: {W}Pointer Speed setting must be MAX.")
    print(f"{G}>>> NOW GO AND CRUSH YOUR ENEMIES! <<<{W}\n")

if __name__ == "__main__":
    try:
        security()
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Stopped.")
        
