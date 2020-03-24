      ▄▄            ▗▖
 ▐▛▀  ▐▌            ▐▌              ▐▌
▐███ ▐███ ▐▙█▙      ▐▙█▙  █▟█▌▐▌ ▐▌▐███  ▟█▙
 ▐▌   ▐▌  ▐▛ ▜▌     ▐▛ ▜▌ █▘  ▐▌ ▐▌ ▐▌  ▐▙▄▟▌
 ▐▌   ▐▌  ▐▌ ▐▌     ▐▌ ▐▌ █   ▐▌ ▐▌ ▐▌  ▐▛▀▀▘
 ▐▌   ▐▙▄ ▐█▄█▘     ▐█▄█▘ █   ▐▙▄█▌ ▐▙▄ ▝█▄▄▌
 ▝▘    ▀▀ ▐▌▀▘      ▝▘▀▘  ▀    ▀▀▝▘  ▀▀  ▝▀▀
          ▐▌  

                                 _                   _           __
\    /._o_|__|_ _ ._  |_    |_) _ ._ _  _  _  _ /   |_  _ ._/__  ._  _
 \/\/ | | |_ |_(/_| | |_)\/ | \(_)| | |(/_(_)_> \_\/|_)(/_| \_|\/|_)_>\/
                         /                        /            / |    / 
Bruteforce speed can be changed in the code by modifying the sleep time after starting each thread.
Happy hacking!!

Usage: ftp_brute.py [options]

Options:
  -h, --help            show this help message and exit
  --target-ip=TARGET_IP
                        Target host or url
  --username=USERNAME   Target username
  --wordlist=WORDLIST   File containing passwords one per line
  --port=PORT           Target FTP port. Defaults to 21

Example usage: 
- Before usage, set up your python ready for using this script as follows:
	python3 -m pip install -r requirements.txt
- Bruteforcing an ftp server with ip 50.142.22.12 with a username root;
	python3 --target-ip=50.142.22.12 --username=root --wordlist=/root/romeos/rockyou.txt --port=21
