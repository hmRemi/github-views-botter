import os
import time
import ctypes
import requests
import threading
from util.logger import *

username = "" # Replace with your proxy
password = "" # Replace with your proxy
proxy = "" # Replace with your proxy
proxy_string = {"http":"http://{}:{}@{}".format(username, password, proxy)}

class info():
    version = "1.0.0"
    author = "✟"

class stats():
    hits = 0
    failed = 0

ctypes.windll.kernel32.SetConsoleTitleW(f"Github Views Botter | Hits: {stats.hits} | Failed {stats.failed} | by {info.author} | v{info.version} | VPM: 0")
os.system("cls")

# Track the start time
start_time = time.time()

# Create a lock to synchronize access to stats.hits and stats.failed
stats_lock = threading.Lock()

def update_console_title():
    global stats
    while True:
        elapsed_time = time.time() - start_time
        views_per_minute = (stats.hits / elapsed_time) * 60
        title = f"Github Views Botter | Hits: {stats.hits} | Failed {stats.failed} | VPM: {views_per_minute:.2f} | by {info.author} | v{info.version}"
        ctypes.windll.kernel32.SetConsoleTitleW(title)
        time.sleep(1)

# Start the title update thread
title_thread = threading.Thread(target=update_console_title)
title_thread.daemon = True
title_thread.start()

print(f"""{Fore.LIGHTRED_EX}
==========================================================================

        ██╗   ██╗██╗███████╗██╗    ██╗    ██████╗  ██████╗ ████████╗
        ██║   ██║██║██╔════╝██║    ██║    ██╔══██╗██╔═══██╗╚══██╔══╝
        ██║   ██║██║█████╗  ██║ █╗ ██║    ██████╔╝██║   ██║   ██║   
        ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║    ██╔══██╗██║   ██║   ██║   
         ╚████╔╝ ██║███████╗╚███╔███╔╝    ██████╔╝╚██████╔╝   ██║   
          ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝     ╚═════╝  ╚═════╝    ╚═╝
                                by {info.author} | v{info.version}
==========================================================================""")

threads = int(logger.input("Enter amount of threads: "))
image_url = logger.input("Enter image url: ")

headers = {
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

def add_view():
    global stats

    r = requests.get(f'{image_url}', headers=headers, proxies=proxy_string)

    if r.status_code == 200 or r.status_code == 201:
        with stats_lock:
            stats.hits += 1
        logger.success(f'Added %d total views' % stats.hits, str(r.reason), str(r.status_code))
    else:
        with stats_lock:
            stats.failed += 1
        logger.error(f'Failed to add view', str(r.reason), str(r.status_code))

while True:
    if threading.active_count() < threads:
        for x in range(threads):
            threading.Thread(target=add_view).start()
