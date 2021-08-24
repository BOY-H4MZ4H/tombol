#!/usr/bin/python2
# -*- coding: utf-8 -*-


#######################################################
#                     OPEN SOURCE                     #
#          JIKA MAU DI RECOD SERTAKAN AUTHOR          #
#        SCRIPT INI DI RAKIT OLEH SAYA SENDIRI        #
#                   AUTHOR BOY HAMZAH                 #
#                                                     #
#                MY TEAM HECKER BEAUTIFUL             #
# ANGGA,BOY,YAYAN,ZACKY,RIZKY,IQBAL,LATIF,HAN, FALLEN #
#######################################################


import os,sys,time
from time import sleep

os.system("clear")

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(3.0 / 200)

def kata(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
    
os.system('clear')  

logo=""" \033[0;92m_______  _____  _______ ______   _____        
    |    |     | |  |  | |_____] |     | |     
    |    |_____| |  |  | |_____] |_____| |_____
    
 \033[0m_______ _______  ______ _______ _     _ _     _
    |    |______ |_____/ |  |  | |     |  \___/ 
    |    |______ |    \_ |  |  | |_____| _/   \_

\033[0mAU > \033[0;92mBoy Hamzah
\033[0mFB > \033[0;92mhttps://www.facebook.com/Boy.Hamzaah
\033[0mGH > \033[0;92mhttps://github.com/BOY-H4MZ4H                              
"""
                                                               
jalan(' \033[0m_______  _____  _______ ______   _____        ')
jalan('    \033[0;92m|    |     | |  |  | |_____] |     | |     ')
jalan('    \033[0m|    |_____| |  |  | |_____] |_____| |_____')
jalan(' \033[0;92m_______ _______  ______ _______ _     _ _     _')
jalan('    \033[0m|    |______ |_____/ |  |  | |     |  \___/ ')
jalan('    \033[0;92m|    |______ |    \_ |  |  | |_____| _/   \_')
print                                           
print('\t     \033[0mCREATE TOO \033[0;92mBOY HAMZAH\033[0m')

                                
def boyHamzaH():
		kata('\033[0m\n\nMenambah Kan Tombol Di Mulai....')
		sleep(1)
		print
		jalan('\033[0mPENEMUAN KUNCI TAMBAHAN TERMUX')
		sleep(1.5)
		print('\033[0;92mBerhasil...')
		sleep(1.2)
		try:
			os.mkdir('/data/data/com.termux/files/home/.termux')
		except:
				pass
				jalan('\033[0mMEMBUAT FILE SETUP')
				sleep(1.5)
				print('\033[0;92mBerhasil...')
				sleep(1.2)
				key = "extra-keys = [['HOME','UP','END','ESC'],['pwd','CTRL','ALT','LEFT','DOWN','RIGHT','TAB']]"
				boy = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
				boy.write(key)
				boy.close()
				sleep(1)
				jalan('\033[0mMENYEBARKAN PENGATURAN KUNCI TAMBAHAN')
				sleep(1.5)
				os.system('termux-reload-settings')
				print('\033[0;92mBerhasil...')
				sleep(1.2)
				print
				kata('\033[0mMenambah Kan Tombol TERMUX Sudah Berhasil...\nSilahkan Ketik $ exit Lalu Enter Dan Kembali Lagi Di Termux')
				sleep(1.7)
				os.system('xdg-open https://www.facebook.com/Boy.Hamzaah')
				sleep(1)
				os.system("clear")
				print (logo)
				print


if __name__ == '__main__':
	boyHamzaH()
