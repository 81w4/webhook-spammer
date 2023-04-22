from colorama import Fore
from dhooks import Webhook
import os
import time
import platform

ver = platform.release()
os.system("mode con: cols=140 lines=30")

def clear():
    os.system("cls")

def logowin10():
    print(f"""
        {Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}    ██{Fore.RED}╗{Fore.WHITE}███████{Fore.RED}╗{Fore.WHITE}██████{Fore.RED}╗{Fore.WHITE} ██{Fore.RED}╗{Fore.WHITE}  ██{Fore.RED}╗{Fore.WHITE} ██████{Fore.RED}╗{Fore.WHITE}  ██████{Fore.RED}╗ {Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}  ██{Fore.RED}╗{Fore.WHITE}    ███████{Fore.RED}╗{Fore.WHITE}███████{Fore.RED}╗{Fore.WHITE}███{Fore.RED}╗{Fore.WHITE}   ██{Fore.RED}╗{Fore.WHITE}██████{Fore.RED}╗{Fore.WHITE} ███████{Fore.RED}╗{Fore.WHITE}██████{Fore.RED}╗{Fore.WHITE} 
        {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}    ██{Fore.RED}║{Fore.WHITE}██{Fore.RED}╔════╝{Fore.WHITE}██{Fore.RED}╔══{Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}██{Fore.RED}║  {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}╔═══{Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}██{Fore.RED}╔═══{Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}██{Fore.RED}║ {Fore.WHITE}██{Fore.RED}╔╝    {Fore.WHITE}██{Fore.RED}╔════╝{Fore.WHITE}██{Fore.RED}╔════╝{Fore.WHITE}████{Fore.RED}╗  {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}╔══{Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}██{Fore.RED}╔════╝{Fore.WHITE}██{Fore.RED}╔══{Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}
        {Fore.WHITE}██{Fore.RED}║ {Fore.WHITE}█{Fore.RED}╗ {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}█████{Fore.RED}╗  {Fore.WHITE}██████{Fore.RED}╔╝{Fore.WHITE}███████{Fore.RED}║{Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}█████{Fore.RED}╔╝     {Fore.WHITE}███████{Fore.RED}╗{Fore.WHITE}█████{Fore.RED}╗{Fore.WHITE}  ██{Fore.RED}╔{Fore.WHITE}██{Fore.RED}╗{Fore.WHITE} ██{Fore.RED}║{Fore.WHITE}██{Fore.RED}║{Fore.WHITE}  ██{Fore.RED}║{Fore.WHITE}█████{Fore.RED}╗  {Fore.WHITE}██████{Fore.RED}╔╝{Fore.WHITE}
        {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}███{Fore.RED}╗{Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}╔══╝  {Fore.WHITE}██{Fore.RED}╔══{Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}██{Fore.RED}╔══{Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}╔═{Fore.WHITE}██{Fore.RED}╗     ╚════{Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}╔══╝  {Fore.WHITE}██{Fore.RED}║╚{Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}║  {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}╔══╝  {Fore.WHITE}██{Fore.RED}╔══{Fore.WHITE}██{Fore.RED}╗
        {Fore.RED}╚{Fore.WHITE}███{Fore.RED}╔{Fore.WHITE}███{Fore.RED}╔╝{Fore.WHITE}███████{Fore.RED}╗{Fore.WHITE}██████{Fore.RED}╔╝{Fore.WHITE}██{Fore.RED}║  {Fore.WHITE}██{Fore.RED}║╚{Fore.WHITE}██████{Fore.RED}╔╝╚{Fore.WHITE}██████{Fore.RED}╔╝{Fore.WHITE}██{Fore.RED}║  {Fore.WHITE}██{Fore.RED}╗    {Fore.WHITE}███████{Fore.RED}║{Fore.WHITE}███████{Fore.RED}╗{Fore.WHITE}██{Fore.RED}║ ╚{Fore.WHITE}████{Fore.RED}║{Fore.WHITE}██████{Fore.RED}╔╝{Fore.WHITE}███████{Fore.RED}╗{Fore.WHITE}██{Fore.RED}║  {Fore.WHITE}██{Fore.RED}║
        {Fore.RED} ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
        {Fore.BLUE} MADE BY 81w_4
    """)
    
  

def boxwin10():
    print(f"""
                                         {Fore.WHITE}      ╭――――――――――――――――――――――――――――――――――╮
                                         {Fore.WHITE}      │                                  │
                                         {Fore.WHITE}      │       {Fore.RED}[1] Send single msg        {Fore.WHITE}│
                                         {Fore.WHITE}      │                                  │
                                         {Fore.WHITE}      │            {Fore.RED}[2] Spam              {Fore.WHITE}│
                                         {Fore.WHITE}      │                                  │
                                         {Fore.WHITE}      │       {Fore.RED}[3] Delete webhook         {Fore.WHITE}│
                                         {Fore.WHITE}      │                                  │
                                         {Fore.WHITE}      ╰――――――――――――――――――――――――――――――――――╯
    
    
    
    """)


def single():
    whe = input(f"{Fore.RED}Link : ")
    msg = input(f"{Fore.RED}Message : ")
    try:
        wh = Webhook(whe)
        wh.send(msg)
        print(f"{Fore.GREEN}Sent {Fore.RED}{msg} to {Fore.GREEN}{whe}!")
        time.sleep(3)
        clear()
        main_loop()
    except ValueError:
        print(f"{Fore.RED}Invalid Webhook URL!")    
        time.sleep(3)
        clear()
        main_loop()
        
def spam():
    whe = input(f"{Fore.RED}Link : ")
    msg = input(f"{Fore.RED}Message : ")
    times = int(input(f"{Fore.RED}How many messages : "))
    if int(times) == int:
       print(f"{Fore.RED} re")
    elif int(times) != int:
       print("e")    
    try:
        wh = Webhook(whe)
        for i in range(int(times)):
            wh.send(msg)
            print(f"{Fore.GREEN}Sent {Fore.RED}{msg} to {Fore.GREEN}{whe}!")
        clear()
        main_loop()
    except ValueError:
        print(f"{Fore.RED}Invalid Webhook URL!")    
        time.sleep(3)
        clear()
        main_loop()

def delete():
    whe = input(f"{Fore.RED}Link : ")

    try:
        wh = Webhook(whe)
        wh.delete()
        print(f"{Fore.GREEN}Deleted {Fore.RED}{whe}!")
        time.sleep(3)
        clear()
        main_loop()
        
    except ValueError:
        print(f"{Fore.RED}Invalid Webhook URL!")    
        time.sleep(3)
        clear()
        main_loop()  
    
        
    
def main_loop():
    logo()
    box()
    option = input(f"{Fore.RED}>>: ")
    if option == "1":
       single()
    elif option == "2":
       spam()
    elif option == "3":
       delete()  
    else:
       print(f"{Fore.RED} Invalid choice.")
       time.sleep(3)
       clear()
       main_loop()
       
main_loop()       
        
