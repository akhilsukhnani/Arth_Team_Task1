import os
from platform import system

def aws_menu():
	if system() == 'Linux':
		os.system("clear")
		os.system("figlet -f standard -c AWS | lolcat")
		

	elif system() == 'Windows':
		os.system("cls")
		print(aws_logo)


aws_logo = """\033[33m

     ___        ______  
    / \ \      / / ___| 
   / _ \ \ /\ / /\___ \ 
  / ___ \ V  V /  ___) |
 /_/   \_\_/\_/  |____/ 
                        
	                           
	\033[97m """

def aws_list():
	print("""\033[33m
				\033[32mChoose Your Option

		\033[36m[1] EC2 Instances  
		\033[36m[2] EBS
		\033[36m[3] Connect EC2 to EBS  
		\033[36m[4] Key Pair
		\033[36m[5] Security Group
		\033[91m[6] New feature will added......
	\033[97m """)

	y = input("Choice ==>>  ")




aws_menu()
aws_list()