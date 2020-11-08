import os 
from platform import system


def menu():
	print("""
        [1] Hadoop 
        [2] Docker 
        [3] AWS CLI
        [4] Basic Linux
        [5] SSH
	\033[91m[99] Exit From The Software [99]
       \033[97m """)
	x = int(input("Choice =>> "))
	if x == 1 :
		os.system("python3 ./hadoop.py")
	elif x == 2 :
		os.system("python3 ./docker.py")
	elif x == 3 :
		os.system("python3 ./aws.py")
	elif x == 4 :
		os.system("python3 ./basic_linux.py")
	elif x == 99 :
		os.system("echo 'Hope You Like This :) Cya! Exiting.....' | lolcat -a -d 100")
		exit()
	else :
		dist_check()
		#os.system("echo ' Hello, You are choosing the wrong option please press currect one' | lolcat -a -d 50")

    


logo = """\033[33m
	 █████╗ ██████╗ ████████╗██╗  ██╗    ██████╗  ██████╗ ██████╗  ██████╗    ██╗ █████╗    ██╗ ██████╗ 
	██╔══██╗██╔══██╗╚══██╔══╝██║  ██║    ╚════██╗██╔═████╗╚════██╗██╔═████╗  ███║██╔══██╗  ███║██╔═████╗
	███████║██████╔╝   ██║   ███████║     █████╔╝██║██╔██║ █████╔╝██║██╔██║  ╚██║╚█████╔╝  ╚██║██║██╔██║
	██╔══██║██╔══██╗   ██║   ██╔══██║    ██╔═══╝ ████╔╝██║██╔═══╝ ████╔╝██║   ██║██╔══██╗   ██║████╔╝██║
	██║  ██║██║  ██║   ██║   ██║  ██║    ███████╗╚██████╔╝███████╗╚██████╔╝██╗██║╚█████╔╝██╗██║╚██████╔╝
	╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝╚═╝ ╚════╝ ╚═╝╚═╝ ╚═════╝ 
	                                                                                                                        
	                            \033[34m[✔] Leader: Kunal Maheshwari       [✔]
	                            \033[34m[✔] Team Member 1: Kadambari More  [✔]
	                            \033[34m[✔] Team Member 2: Muskan Agarwala [✔]
	                            \033[34m[✔] Team Member 3: Pradeep Kumar   [✔]
	                            \033[34m[✔] Team Member 4: Rahul Kumar     [✔]	

	                            \033[91m[✔]           Menu                 [✔]
	\033[97m """	



def dist_check():
	if system() == 'Linux':
		os.system("clear")
		print(logo)
		menu()
	elif system() == 'Windows':
		os.system("cls")
		print(logo)
		menu()
dist_check()

