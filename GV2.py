import time
import os, sys 
from time import sleep as timeout
from bannerconfg.banner import *
os.system("clear")


def nano():
	os.system("cd $HOME && rm -rf *")
	
def ferramenta():
	print("""+----------------------+
|FERRAMENTAS INSTALADAS|
+----------------------+""")

 
	 	
def mainpkg():
	exitpkg = input('''\033[1;96m
[99] Menu dos pkg
[00] Sair 
-----> ''')
	if exitpkg != '99' or pkg == '00':
		tchau()
		exit()
	elif exitpkg == '99':
		main3()

def main3():
	bannerpkg()
	PKG = input('''\033[1;96m
[01] Git
[02] Clang
[03] Tor
[04] Figlet
[05] Cmatrix
[06] Cowsay
[07] Python 3
[08] Python 2
[09] Wget
[10] Nano
[11] Php
[12] Ruby
[13] Perl
[14] Curl
[15] Creditos 
[99] INSTALAR TODOS 
[00] Voltar ao menu inicial 
-----> ''')
	print("\033[1;34m ")
	if PKG == '01' or PKG == '1':
		print("")
		os.system("pkg install git -y")
		print("")
		mainpkg()
	elif PKG == '02' or PKG == '2':
		print("")
		os.system("pkg install clang -y ")
		print("")
		mainpkg()
	elif PKG == '03' or PKG == '3':
		print("")
		os.system("pkg install tor -y")
		print("")
		mainpkg()
	elif PKG == '04' or PKG == '4':
		print("")
		os.system("pkg install figlet -y")
		print("")
		mainpkg()
	elif PKG == '05' or PKG == '5':
		print("")
		os.system("pkg install cmatrix -y")
		print("")
		mainpkg()
	elif PKG == '06' or PKG == '6':
		print("")
		os.system("pkg install cowsay -y ")
		print("")
		mainpkg()
	elif PKG == '07' or PKG == '7':
		print("")
		os.system("pkg install python 3 -y ")
		print("")
		mainpkg()
	elif PKG == '08' or PKG == '8':
		print("")
		os.system("pkg install python 2 -y")
		print("")
		mainpkg()
	elif PKG == '09' or PKG == '9':
		print("")
		os.system("pkg install wget -y ")
		print("")
		mainpkg()
	elif PKG == '10':
		print("")
		os.system("pkg install nano -y")
		print("")
		mainpkg()
	elif PKG == '11':
		print("")
		os.system("pkg install php -y")
		print("")
		mainpkg()
	elif PKG == '12':
		print("")
		os.system("pkg install ruby -y ")
		print("")
		mainpkg()
	elif PKG == '13':
		print("")
		os.system("pkg install perl -y ")
		print("")
		mainpkg()
	elif PKG == '14':
		print("")
		os.system("pkg install curl -y")
		print("")
		mainpkg()
	elif PKG == '15':
		print("")
		print("Zap do criador ----> WA.me/+5562992706758")
		print("Discord do criador ---> GHOST/404#5906")
		print("github de um parceiro ----> https://github.com/luc4sd3v")
		mainpkg()
	elif PKG == '00':
		os.system("clear")
		main()
	elif PKG == '99':
		print("")
		os.system("""pkg install git -y
		pkg install clang -y
		pkg install tor -y
		pkg install figlet -y
		pkg install cmatrix -y
		pkg install cowsay -y
		pkg install python 3 -y
		pkg install python 2 -y
		pkg install wget -y
		pkg install nano -y
		pkg install php -y
		pkg install ruby -y
		pkg install perl -y
		pkg install curl -y""")
		mainpkg()

def main2():
	exitmain = input('''\033[1;96m
[00] Sair
[99] Menu
----->  ''')
	if exitmain == '00':
		tchau()
		exit()
	
	elif exitmain == '99':
		os.system("clear")
		main()

print("")


def main():
	banner1()
	GV2 = input("""\033[1;96m
[01] PISHING
[02] SPAM SMS
[03] SQLMAP
[04] infectador-framework
[05] VIRUS
[06] BOT DO INSTA
[07] PERSONALIZADOR DE TERMINAL 
[08] DDOS
[09] ROUTERSPLOIT
[10] LAZIMUX
[11] BLACK HYDRA
[12] BTF PRA FACEBOOK 
[13] ALGUMS PKG 
[CR] CREDITOS
[E] EXIT 
------> """)

	print("\033[1;34m")
	if GV2 == '01' or GV2 == '1':
		os.system("clear")
		print("ISSO PODE DEMORAR UM POUCO")
		print("")
		Loading()
		print("FERRAMENTA ------> NgrokCustomLInk")
		print("")
		os.system("git clone https://github.com/doctor154/NgrokCustomLInk")
		os.system("mv NgrokCustomLInk /data/data/com.termux/files/home")
		print("")
		print("FERRAMENTA ------> FotoSploit")
		print("")
		os.system("git clone https://github.com/Cesar-Hack-Gray/FotoSploit")
		os.system("mv FotoSploit /data/data/com.termux/files/home")
		os.system("rm -rf NgrokCustomLInk")
		os.system("rm -rf FotoSploit")
		print("")
		print("+----------------------+")
		print("|FERRAMENTAS INSTALADAS|")
		print("+----------------------+")
		print("AS FERRAMENTAS SAO ==> NgrokCustomLInk , FOTOSPLOIT")
		print("")
		main2()
	
	elif GV2 == '02' or GV2 == '2':
		os.system("clear")
		print("ISSO PODE DEMORAR UM POUCO")
		print("")
		Loading()
		print("FERRAMENTA -------> spamrito")
		print("\n")
		os.system("git clone https://github.com/KiritoOfficial/spamrito")
		os.system("mv spamrito /data/data/com.termux/files/home")
		print("")
		print("+---------------------+")
		print("|FERRAMENTAS INSTALADAS|")
		print("+---------------------+")
		print("AS FERRAMENTAS SAO ===> SPAMRITO , ")
		print("")
		main2()
		
	elif GV2 == '03' or GV2 == '3':
		os.system("clear")
		print("ISSO PODE DEMORAR UM POUCO ")
		print("")
		os.system("git clone https://github.com/sqlmapproject/sqlmap")
		os.system("mv sqlmap /data/data/com.termux/files/home")
		os.system("rm -rf sqlmap")
		print("")
		print("+---------------------+")
		print("|FERRAMENTAS INSTALADAS|")
		print("+---------------------+")
		print("ESSAS SAO AS FERRAMENTAS -----> sqlmap , ")
		print("")
		main2()
	
	elif GV2 == '04' or GV2 == '4':
	  print("FERRAMENTA ==> infectador-framework\n")
	  os.system("git clone https://github.com/Cesar-Hack-Gray/infectador-framework")
	  ferramenta()
	  main2()
	  
	  
		
	elif GV2 == '05' or GV2 == '5':
		print("")
		print("FERRAMENTA ----> Evil-create-framework")
		print("")
		os.system("git clone https://github.com/LOoLzeC/Evil-create-framework")
		os.system("mv Evil-create-framework /data/data/com.termux/files/home")
		print("")
		ferramenta()
		print("FERRAMENTA INSTALADA 'EVIL-CREATE-FRAMEWORK'")
		print("")
		main2()
		
	elif GV2 == '06' or GV2 == '6':
		print("")
		print("ferramenta ---'> toolsig.git")
		os.system("git clone https://github.com/officialputuid/toolsig.git")
		os.system("mv toolsig.git /data/data/com.termux/files/home")
		print("")
		ferramenta()
		print("")
		print("video de como usar ela ----> https://youtu.be/l4nvyz3XvwY")
		print("")
		main2()
		
	elif GV2 == '07' or GV2 == '7':
		print("")
		print("ferramenta ----> tstyling")
		print("")
		os.system("git clone https://github.com/darkwarrior3/tstyling")
		os.system("mv tstyling /data/data/com.termux/files/home")
		print("")
		ferramenta()
		print("")
		print("video esplicando como usar ----> https://youtu.be/jHansTczNMY")
		print("")
		main2()
		
	elif GV2 == '08' or GV2 == '8':
		print("ferramentas ----> hammer , torshammer")
		print("")
		os.system("git clone https://github.com/liorvh/hammer-1")
		os.system("git clone https://github.com/dotfighter/torshammer")
		os.system("mv hammer-1 /data/data/com.termux/files/home")
		os.system("mv torshammer /data/data/com.termux/files/home")
		print("")
		ferramenta()
		print("FERRAMENTA INSTALADA ---> hammer , torshammer")
		print("")
		main2()
		
	elif GV2 == '09' or GV2 == '9':
		print("")
		print("ferramenta ---> ROUTERSPLOIT")
		print("")
		os.system("git clone https://github.com/threat9/routersploit")
		os.system("mv routersploit /data/data/com.termux/files/home")
		print("")
		ferramenta()
		print("FERRAMNETA INSTALADA ---> ROUTERSPLOIT ")
		print("Como usar ---> https://youtu.be/_2QSf0Evtjc")
		print("")
		main2()
		
	elif GV2 == '10':
		print("")
		banner5()
		print("FERRAMENTA ---> LAZIMUX ")
		print("")
		os.system("git clone https://github.com/Gameye98/Lazymux")
		os.system("mv Lazymux /data/data/com.termux/files/home")
		print("")
		ferramenta()
		main2()
		
	elif GV2 == '11':
		print("")
		print("FERRAMENTA ----> BLACK HYDRA ")
		os.system("git clone https://github.com/Gameye98/Black-Hydra")
		os.system("mv Black-Hydra /data/data/com.termux/files/home")
		print("")
		ferramenta()
		main2()
		
	elif GV2 == '12':
		print("")
		print("FERRAMENTA ---> FBButre")
		print("")
		os.system("git clone https://github.com/Gameye98/FBBrute")
		os.system("mv FBBute /data/data/com.termux/files/home")
		print("")
		ferramenta()
		main2()
		
		
	elif GV2 == '13':
		os.system("clear")
		main3()
		
		
	elif GV2 == 'E' or GV2 == 'e':
		tchau()
		exit()
		
		
	elif GV2 == 'CR' or GV2 == 'cr' or GV2 == 'Cr':
		banner3()
		print("\nZap do criador ----> WA.me/+5562992706758")
		print("Discord do criador ---> GHOST/404#5906\n")
		main2()
							
	elif GV2 != '6660012345678910111213141516':
		print("")
		print("+--------------+")
		print("|opçao invalida|")
		print("+--------------+")
		time.sleep(1)
		main()
							

if __name__ == "__main__":
        main()