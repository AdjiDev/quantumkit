"""
Gratis rekod loss sana hus hus

Rizky Kian Adji (c) 2024

"""

import sys
import os
from time import sleep as turu
from colorama import Fore, init, Style

init()

merah = Fore.RED
kuning = Fore.YELLOW
hijau = Fore.GREEN
biru = Fore.BLUE
hitam = Fore.BLACK
cyan = Fore.CYAN
ungu = Fore.MAGENTA
putih = Fore.WHITE
cerah = Style.BRIGHT

banner = f"""
{cerah}{kuning}─────────────────────────────────────────────                                             
{cerah}{merah} _____             _             _____ _ _   
{cerah}{merah}|     |_ _ ___ ___| |_ _ _ _____|  |  |_| |_  {hijau}# Version alpha_0.0.1
{cerah}{merah}|  |  | | | .'|   |  _| | |     |    -| |  _| {kuning}# Kiddies Kit for beginner
{cerah}{putih}|__  _|___|__,|_|_|_| |___|_|_|_|__|__|_|_|   {cerah}{ungu}# AdjiDev (C) 2024
{cerah}{putih}   |__|
{cerah}{kuning}──────────────────────────────────────────────
{ungu}[01] {hijau}AI CHAT                                     
{ungu}[02] {hijau}WIFI FLOODER                                  
{ungu}[03] {hijau}DNS LOOKUP                                 
{ungu}[04] {hijau}PHONENUM LOOKUP
{cerah}{kuning}──────────────────────────────────────────────
"""

def ngetik(teks):
    for i in teks:
        sys.stdout.write(i)
        sys.stdout.flush()
        turu(0.003)

def dasbor():
    os.system('cls' if os.name == 'nt' else 'clear')
    ngetik(banner)
    while True:
        try:
            pilihan = input(f'{merah}System{cerah}{putih}@{cyan}AdjiDev> ')
            if pilihan == '1':
                ngetik(f'{merah}Wait . . .\n')
                turu(2)
                os.system('cd fitur && python gemini.py')
            elif pilihan == '2':
                ngetik(f'{merah}Wait . . .\n')
                turu(2)
                os.system('cd fitur && python flood.py')
            elif pilihan == '3':
                enter_ip = input(f'{merah}Enter DNS Target IP>{putih} ')
                os.system(f'ping {enter_ip}')
                ngetik(f'{merah}Done.\n')
            elif pilihan == '4':
                ngetik(f'{merah}Wait . . .\n')
                turu(2)
                os.system('cd fitur && numlookup.py')
        except KeyboardInterrupt:
            print(f"\n{merah}Exiting . . .\n")
            turu(2)
            break

dasbor()
