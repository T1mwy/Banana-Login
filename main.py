from msilib.schema import Font
import subprocess
import requests
import time
import json
import sys
import os
import colorama
import ctypes

from json import load
from colorama import Fore
from pystyle import Colors, Colorate , Anime ,Center
from secrets import choice

# Console Title
title = "title Overtime_Gang ^| By Timmy" 

# Text Logo
# You can make a Text in http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
Login_Text = str("""
:::        ::::::::   :::::::: ::::::::::: ::::    ::: 
:+:       :+:    :+: :+:    :+:    :+:     :+:+:   :+: 
+:+       +:+    +:+ +:+           +:+     :+:+:+  +:+ 
+#+       +#+    +:+ :#:           +#+     +#+ +:+ +#+ 
+#+       +#+    +#+ +#+   +#+#    +#+     +#+  +#+#+# 
#+#       #+#    #+# #+#    #+#    #+#     #+#   #+#+# 
########## ########   ######## ########### ###    #### 

[1] Login
[2] Register
[3] Check Hwid
[4] Exit
""")

UI = """
         ██████╗ ██╗   ██╗███████╗██████╗ ████████╗██╗███╗   ███╗███████╗     ██████╗  █████╗ ███╗   ██╗ ██████╗ 
        ██╔═══██╗██║   ██║██╔════╝██╔══██╗╚══██╔══╝██║████╗ ████║██╔════╝    ██╔════╝ ██╔══██╗████╗  ██║██╔════╝ 
        ██║   ██║██║   ██║█████╗  ██████╔╝   ██║   ██║██╔████╔██║█████╗      ██║  ███╗███████║██╔██╗ ██║██║  ███╗
        ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██║██║╚██╔╝██║██╔══╝      ██║   ██║██╔══██║██║╚██╗██║██║   ██║
        ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║   ██║   ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝██║  ██║██║ ╚████║╚██████╔╝
         ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ """

# Get hwid
HWID = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()

# Data
# https://pastebin.com
Data_Hwid = requests.get("")
Data_Un = requests.get("")
Data_Pw = requests.get("")

# Webhook link
WB_URL = ""
Dev_id = ""
Discord_User = "" # test#12345
Email = ""
Github_link = ""

def ST(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(0.2)

# Login System
def Login():
    os.system(title)
    os.system("cls")
    print(Colorate.Horizontal(Colors.yellow_to_red, Login_Text))
    LAR = input(f"\n{Fore.YELLOW}[{Fore.GREEN}>>>{Fore.YELLOW}]{Fore.WHITE}Choice : ")
    os.system("cls")
    if LAR == '1':
        Username = input(f"{Fore.GREEN}Username: {Fore.RED}{Fore.RESET}")
        if Username in Data_Un.text:
            Password = input(f"{Fore.GREEN}Password: {Fore.RED}{Fore.RESET}")
            if Password in Data_Pw.text:
                os.system("cls")
                print("[+]Login Success")
                time.sleep(2)
                os.system("cls")
                Main()

            else:
                print("Invalid password")
                time.sleep(2)
                os.system("cls")
                Login()

        else:
            print("Invalid username")
            time.sleep(2)
            os.system("cls")
            Login()

    elif LAR == '2':
        os.system("cls")
        print(f"{Fore.LIGHTGREEN_EX}Your Hwid : {HWID}{Fore.RESET}")
        RG_Un = input(f"{Fore.LIGHTGREEN_EX}Your Username : {Fore.RESET}")
        RG_Pw = input(f"{Fore.LIGHTGREEN_EX}Your Password : {Fore.RESET}")
        os.system("cls")
        print(f"{Fore.LIGHTGREEN_EX}[+{Fore.LIGHTGREEN_EX}]Register your account success{Fore.RESET}")
        time.sleep(2)
        data = {"content": f'''<@{Dev_id}>\n**New User**\n**HWID : {HWID}**\n**Username : {RG_Un}**\n**Password : {RG_Pw}**'''}
        response = requests.post(WB_URL, json=data)
        print(response.content)
        os.system("cls")
        print(f'''{Fore.RED}
[!]Warning
Wait for the application for about 10 - 50 minutes If you can get it contact the admin

Discord User : {Discord_User}
Email : {Email}
Github : {Github_link}\n{Fore.RESET}''')
        input(f"{Fore.YELLOW}Enter to go back: {Fore.RESET}")
        os.system("cls")
        Login()

    elif LAR == '3':
        os.system("cls")
        print(f"{Fore.LIGHTRED_EX}You HWID: {Fore.LIGHTRED_EX}{HWID}{Fore.RESET}")
        input(f"{Fore.YELLOW}Enter to return : {Fore.RESET}")
        os.system("cls")
        Login()

    elif LAR == '4':
        exit()

    elif LAR != '':
         print("Dont have this choice")
         time.sleep(2)
         os.system("cls")
         Login()
        
# Payload
def Main():
    if HWID in Data_Hwid.text:
        print(UI)
        input("")   #<---------- place your code

    else:
        print("""
        [!]Warning
        Your hwid is not in the database
        You can add your HWID by notifying the administrator
        """)
        input("Enter to register new account")
        os.system("cls")
        Login()

Login()