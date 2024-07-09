import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from time import sleep as turu
import os
import sys
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

banner = f'''
{cerah}{kuning}─────────────────────────────────────────────                                           
{cerah}{hijau} _____           __            _           
{cerah}{hijau}|   | |_ _ _____|  |   ___ ___| |_ _ _ ___ 
{cerah}{putih}| | | | | |     |  |__| . | . | '_| | | . |
{cerah}{putih}|_|___|___|_|_|_|_____|___|___|_,_|___|  _|
                                      |_|
{cerah}{kuning}─────────────────────────────────────────────
{cerah}{hijau}[+] {cerah}{kuning} Type exit back to main menu
{cerah}{kuning}─────────────────────────────────────────────
'''

def ngetik(teks):
    for i in teks:
        sys.stdout.write(i)
        sys.stdout.flush()
        turu(0.04)

kode_area_provinsi = {
    '021': 'DKI Jakarta',
    '022': 'Bandung',
    '031': 'Surabaya',
    '061': 'Medan',
}

def cek_nomor_telepon(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)

        is_valid = phonenumbers.is_valid_number(parsed_number)

        location = geocoder.description_for_number(parsed_number, "id")

        service_provider = carrier.name_for_number(parsed_number, "id")

        time_zones = timezone.time_zones_for_number(parsed_number)

        national_number = str(parsed_number.national_number)
        kode_area = national_number[:3] 
        provinsi = kode_area_provinsi.get(kode_area, "null")

        print(f'\n{merah}=============================================================\n')
        print(f"{cerah}{hijau}phone_number: {cerah}{putih}{phone_number}")
        print(f"{cerah}{hijau}is_valid: {cerah}{putih}{is_valid}")
        print(f"{cerah}{hijau}country: {cerah}{putih}{location}")
        print(f"{cerah}{hijau}Province: {cerah}{putih}{provinsi}")
        print(f"{cerah}{hijau}carrier: {cerah}{putih}{service_provider}")
        print(f"{cerah}{hijau}timezone: {cerah}{putih}{', '.join(time_zones)}")
        print(f'\n{merah}=============================================================\n')

    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"{merah}Error: {str(e)}")

if __name__ == "__main__":
    os.system('clear' if os.name == 'posix' else 'cls')
    print(banner)
    
    while True:
        phone_number = input(f"{cerah}{kuning}Masukkan nomor telepon (atau ketik 'exit' untuk keluar): {cerah}{putih}")
        if phone_number.lower() == 'exit':
            ngetik(f'{merah}wait . . .\n')
            os.system('cd .. & python adji.py')
        cek_nomor_telepon(phone_number)
