from datetime import datetime
from colorama import init, Fore
import threading

lock = threading.RLock()

class logger:
    def debug(text1, text2=None):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        lock.acquire()
        if text2 != None:
            print(
                Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTYELLOW_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTYELLOW_EX + "^" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTYELLOW_EX + text1 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTYELLOW_EX + text2)
        else:
            print(
                Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTYELLOW_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTYELLOW_EX + "^" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTYELLOW_EX + text1)

        lock.release()

    def pending(text1, text2, text3):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        lock.acquire()
        print(
            Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + "/" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTRED_EX + text1 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTRED_EX + text2 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTRED_EX + text3)
        lock.release()


    def success(text1, text2, text3):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        lock.acquire()
        print(
            Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + "*" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTRED_EX + text1 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTRED_EX + text2 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTRED_EX + text3)
        lock.release()

    def error_single_response(text1):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        lock.acquire()
        print(
            Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + "!" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTRED_EX + text1 + Fore.LIGHTBLACK_EX)
        lock.release()

    def error(text1, text2, text3):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        lock.acquire()
        print(
            Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + "!" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTRED_EX + text1 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTRED_EX + text2 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTRED_EX + text3)
        lock.release()

    def input(text):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        print(
            Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + ">" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTRED_EX + text,
            end="")
        return input(Fore.WHITE + "")