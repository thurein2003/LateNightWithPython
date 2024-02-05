#LateNightWithPython
#14.1.2024

from colorama import Fore 
import pyfiglet
import time


font = pyfiglet.figlet_format("Count Down App")
print(Fore.BLUE + font)


def count_number(second):
    while second > 0:
        print(f"Number left {second} second")
        time.sleep(1)
        second = second - 1
    print("Good job")
    
def main():
    try:
        second = int(input("Enter time : "))
        count_number(second)
    except:
        print("Try Again")
        
if __name__ == "__main__":
    main()
        
