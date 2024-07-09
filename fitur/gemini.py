import os
import google.generativeai as genai
from time import sleep as turu
import sys
from colorama import Fore, init, Style
from config import gemini_key

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
{cerah}{cyan} _____ _ _____ _       _   
{cerah}{cyan}|  _  |_|     | |_ ___| |_ 
{cerah}{biru}|     | |   --|   | .'|  _|
{cerah}{biru}|__|__|_|_____|_|_|__,|_| 
{cerah}{kuning}───────────────────────────────────────────── 
{cerah}{ungu}[+] Type {putih}'{merah}Exit{putih}' {cerah}{hijau}back to main dashboard 
"""

genai.configure(api_key=gemini_key)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 1200,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "your name is aili now",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I understand. You can call me Aili now.  😊  How can I help you today? \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "do not use string (** **)",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Got it, Aili will avoid using asterisks (**) for bolding from now on.  What would you like me to do today? \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "and string (```)",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Understood! From now on, Aili will avoid using asterisks (**) for bolding and backticks (```) in responses. \n\nHow can I help you today? \n",
      ],
    },
  ]
)

def ngetik(teks):
    for i in teks:
        sys.stdout.write(i)
        sys.stdout.flush()
        turu(0.003)

def chattingan():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    while True:
        input_teks = input(f'{merah}System{putih}@{cerah}{ungu}Gem{cerah}{cyan}ini>{putih}{cerah}')
        jawabnya = chat_session.send_message(input_teks)
        print(kuning + '\n=================================================================\n')
        ngetik(cyan + jawabnya.text)
        print(kuning + '\n=================================================================\n')
        if input_teks == 'exit':
            ngetik(cerah + cyan + 'Wait  . . .\n')
            ngetik(cerah + cyan +'Bye Bye\n')
            os.system('cd .. & python adji.py')

chattingan()