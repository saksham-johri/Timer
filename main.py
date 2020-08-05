from datetime import date, datetime, timedelta
from pyfiglet import figlet_format
from os import system, name
from time import time, sleep
from win32com.client import Dispatch

#! This program is developed by Saksham.

def clear():
    """To clear the output screen
    """
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def speak(str):
    """Speaks the string in computer audio

    Args:
        str (String): String to speak
    """
    
    speak = Dispatch("SAPI.SpVoice")

    speak.speak(str)

def banner(text):
    """To print the ASCII banner

    Args:
        text (String): String to print in the form of ASCII banner
    """
    ascii_banner = figlet_format(text)
    print(ascii_banner)

def current_date():
    """Returns the current date

    Returns:
        Date: Current Date
    """
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    return d2

def current_time():
    """Returns the current time

    Returns:
        Time: Current Time
    """
    d = datetime.now()
    return(d.strftime('%I:%M:%S %p'))

if __name__ == "__main__":
    banner("#  TIMMER  #")
    print(f"Date: {current_date()}")
    print(f"Time: {current_time()}")

    print("\nEnter time in format HH:MM:SS !")
    time_input = list(map(int, input().split(':')))
    clear()
    
    time_out = int((time_input[0] * 3600) + (time_input[1] * 60) + (time_input[2]))

    init_time = time()

    while True:
        if time() - init_time > time_out:
            clear()
            banner("T I M E  U P  ! !")
            speak("Time Up!! Time Up!! Time Up!!")
            sleep(2)
            break
        
        else:
            clear()
            a = time() - init_time
            temp = timedelta(seconds = a)
            temp = str(temp)
            temp, garbage = temp.split('.')
            banner(temp)
            sleep(1)
