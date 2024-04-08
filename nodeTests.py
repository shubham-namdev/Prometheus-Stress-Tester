import os
import subprocess
from utils import *
import time
import json


with open('config.json', 'r') as f:
    config = json.load(f)

ip = config["ip"]["node_exporter"]


def cpuTest():

    clear()
    print("Overloading CPU.  Press Ctrl+c to exit()")
    try :
        for i in range(100000000000000):
            pass
    except KeyboardInterrupt:
        print('='*25 + '\n' + f":: Testing Ended ::" + '\n' + '='*25)
        time.sleep(1)
        clear()

def memTest():
    clear()
    print("Overloading memory.  Press Ctrl+c to exit()")
    try:
        memory_list = []
        for i in range(120):
            memory_list.extend([0] * 1000000)
        time.sleep(180)

    except KeyboardInterrupt:
        print('='*25 + '\n' + f":: Testing Ended ::" + '\n' + '='*25)
        time.sleep(1)
        clear()

def diskTest():
    subprocess.run('cls', shell=True)
    print_message("Creating Temporary files: ", color='orange')
    with open(r"/root/sample.txt", 'a') as file:
        for i in range(1000000):
            file.write("A"*2000 + '\n')
    print_message("Enter 'q' to quit!", color="magenta")
    f = input(">> ")
    command = 'rm -f /root/sample.txt'
    subprocess.run(command, shell=True)
    subprocess.run('cls', shell=True)
    print('='*25 + '\n' + f":: Testing Ended ::" + '\n' + '='*25)
    time.sleep(1)
    clear()

def networkAttack():
    clear()
    try:
        print_message("Performing DOS attack on host...", color='red')
        print("Press Ctrl+C to exit...")
        command = f' hping3 -d 200 -p 9200 --flood {ip}'
        subprocess.run(command, shell=True)
    except KeyboardInterrupt:
        print('='*25 + '\n' + f":: Testing Ended ::" + '\n' + '='*25)
        time.sleep(1)
        subprocess.run('cls', shell=True)

