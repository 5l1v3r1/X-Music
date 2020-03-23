#!/usr/bin/python
# -*- coding: utf8 -*-
# X-Musik
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/X-Musik

import os, sys, time, subprocess
from random import *
from time import sleep

info = """
Nama        : X-Musik
Versi       : 2.3 (Update: 31 April 2020, 11:00 PM)
Tanggal     : 20 Oktober 2019
Author      : Nedi Senja
Tujuan      : Memutar musik di Terminal (termux)
              dngan mudah
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
               manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: https://tinyurl.com/wel4alo

[ \033[4mGunakan tool ini dengan bijak \033[0m]\n """

example = """\033[0;100;77;1m[          X - Music, My Github: @stepbystepexe          ]\033[0m"""

logo = """
\033[0;91m ▀██  ██▀                                        \033[0;31m▬▬▬
\033[0;91m   ████         \033[0;37m█▀▀█▀▀█ █   █ █▀▀▀▀ ▀▀█▀▀ █▀▀▀▀   \033[0;33m▬▬▬▬
\033[0;91m   ▄██▄   \033[0;96;2m███   \033[0;37m█  █  █ █   █ ▀▀▀▀█   █   █        \033[0;34m▬▬▬▬
\033[0;91m  ▄█▀▀█▄        \033[0;37m▀  ▀  ▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀▀▀▀▀   \033[0;35m▬▬▬▬
\033[0;91m ▀▀▀  ▀▀▀       \033[0;91;1mo  \033[0;92;1m+  \033[0;93;1mo   \033[0;94;1mo     \033[0;95;1m+     \033[0;96;1m*     \033[0;77;1mo    \033[0;32m▬▬▬▬
"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def loads():
    o = [
    ' .   ',' ..  ',' ... ']
    for i in o:
        print '\r\033[0m[\033[0;33m●\033[0m] Sedang memproses'+i,
        sys.stdout.flush()
        time.sleep(1)

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def menu():
    os.system('clear')
    os.system('reset')
    sleep(1)
    print
    print logo
    print example
    print
    print "\033[0m[\033[1;96;2m1\033[0m] \033[1;77mPutar Sekarang"
    print "\033[0m[\033[1;96;2m2\033[0m] \033[1;77mCari Lagu"
    print "\033[0m[\033[1;96;2m3\033[0m] \033[1;77mVidio & Musik"
    print "\033[0m[\033[1;96;2m4\033[0m] \033[1;77mDownloads"
    print
    print "\033[0m[\033[93;1m&\033[0m] LISENSI"
    print "\033[0m[\033[94;1m#\033[0m] Informasi"
    print "\033[0m[\033[92;1m*\033[0m] Perbarui"
    print "\033[0m[\033[91;1m-\033[0m] Keluar"
    print
    option = raw_input("\033[0m(\033[105;77;1m/\033[0m) \033[1;77mMasukan opsi: \033[0m")
    if option.strip() in '1 putar'.split():
        write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
        sleep(1)
        def genlist():
                os.system('clear')
                os.system('reset')
                sleep(1)
                print
                print logo
                print example
                print
                os.system("find -L /sdcard -type f -ipath '*.mp3' >.mp3.list")
                print '\n\033[0m[\033[93;1m*\033[0m] \033[77;1mMengsken \033[0m/storage/musik/list.mp3'
                sleep(1)
                sch = raw_input('\033[0m[\033[95;1m?\033[0m] Sken dari memori [Y/n]: ')
                if sch.lower().strip() == "y":
                        print
                        write("\n\033[0m[\033[31m●\033[0m] \033[77;1mSedang mngsken ...\033[0m")
                        os.system("find -L /storage/A892-D352/ -type f -ipath '*.mp3' >>.mp3.list")
                        sleep(3)
                        print "\033[0m[\033[92;1m#\033[0m] Mengskean selesai"
                raw_input('\n[ Tekan Enter ]')
                dislist()

        def getState():
                f1 = open(".info","r")
                a = f1.read()
                f1.close()
                if len(a) >= 21:
                        return True
                else:
                        return False

        def Exit():
                global p
                ln=open('.mp3.list').read()
                if len(p)!=ln.count('\n'):
                        print "\n\033[0m[\033[91;1m!\033[0m] Keluar dari program!"
                        f=open('.mp3.list','w')
                        for wr in p:
                                f.write(wr+'\n')
                        f.close()
                        sys.exit(1)

        def dislist():
                global p
                global sname
                f=open(".mp3.list","r")
                a=f.read()
                f.close()
                p=a.split("\n")
                p.remove('')
                sname=[]
                flg=True
                while flg:
                        flg1=True
                        for pr in p:
                                if not os.path.exists(pr):
                                        p.remove(pr)
                                        flg1=False
                        if flg1:
                                flg=False
                cols=int(os.popen('echo $COLUMNS').read().split('\n')[0])
                for pr in p:
                        l=pr.rfind('/')+1
                        if l==0:
                                continue
                        ap=pr[l:len(pr)-4]
                        dif=len(ap)-cols+30
                        if dif>0:
                                ap=ap[:len(ap)-dif]
                        sname.append(ap)
                if len(p) ==0:
                        print "\033[0m[\033[96;1m+\033[0m] Musik tidak ditemukan"
                        print "\033[0m[\033[93;1m*\033[0m] Lagu dengan ekstensi .mp3 hanya dikenali"
                        Exit()
                print str(len(p))

        def sortlist():
                global p
                ln=open('.mp3.list').read()
                if len(p)!=ln.count('\n'):
                        print "\033[0m[\033[93;1m*\033[0m] Silahkan menunggu"
                        f=open('.mp3.list','w')
                        for wr in p:
                                f.write(wr+'\n')
                                f.close()
                        print "Selesai mebyimpan"
                print '\n\033[0m[\033[94;1m#\033[0m] \033[77;1mSedang menyort daftar'
                os.system('sort -bfidu mp3.list -o mp3.list')
                dislist()

        def remove(n):
                global p
                global sname
                p.pop(n)
                sname.pop(n)
        if not os.path.isfile('.mp3.list'):
                genlist()

        f=open(".mp3.list","r")
        a=f.read()
        f.close()
        p=a.split("\n")
        p.remove('')
        sname=[]
        flg=True
        while flg:
            flg1=True
            for pr in p:
                    if not os.path.exists(pr):
                            p.remove(pr)
                            flg1=False
            if flg1:
                    flg=False
        if len(p) ==0:
            print
            print
            Exit()
        cols=int(os.popen('echo $COLUMNS').read().split('\n')[0])
        for pr in p:
            l=pr.rfind('/')+1
            if l==0:
                    continue
            ap=pr[l:len(pr)-4]
            dif=len(ap)-cols+30
            if dif>0:
                    ap=ap[:len(ap)-dif]
            sname.append(ap)

        n=0
        k=randint(0,len(p)-1)
        n=k
        pos=0
        empl=500+len(p)*10
        while n < len(p):
            fg=True
            cols=int(os.popen('echo $COLUMNS').read().split('\n')[0])
            lin= cols
            flag=True
            for cl in range(0,empl):
                    print
            os.system('clear')
            os.system('reset')
            sleep(1)
            print
            print logo
            print example
            print
            write("\033[0m[ \033[32mINFO \033[0m] \033[3mGunakan headset (earphone) biar lebih kennceeeng")
            write("         Sediakan kopi, roko + cemilan biar lebih mantaps\033[0m\n\n")
            sleep(1)
            for i in range(0,len(p)):
                    if i==n:
                            print "\033[0m[\033[96;2;1m"+str(i+1)+"\033[0m]  \033[91;1m-->  \033[0m"+sname[i]+"   \033[77;1m(\033[93;1mMemutar\033[0;77;1m)\033[0m"
                            sleep(0.05)
                    else:
                            print "\033[0m[\033[96;2;1m"+str(i+1)+"\033[0m]       \033[0m"+sname[i]
                            sleep(0.05)

            playing=True
            try:
                    write("\n\033[0m[\033[31m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
                    sleep(3)
                    if not getState() or pos!=n:
                            pos=n
                            os.system('clear')
                            os.system('reset')
                            sleep(1)
                            print
                            print logo
                            print example
                            print
                            print '\033[0mFrom \033[91;2m/storage/sdcard/'
                            print '\033[0mSedang mendengarkan (memutar) \033[96;2mmusik Anda...\033[0m'
                            print
                            print "\033[77;4;1mTekan Ctrl + C untuk kembali\033[0m"
                            print
                            subprocess.call(["mpv \""+p[pos]+"\""],shell=True)
            except KeyboardInterrupt:
                    print
                    print
                    print "\033[0m[\033[91;1m!\033[0m] \033[77;1mKembali\033[0m"
                    print
                    sleep(1)
                    menu()

            ref=False
            while True:
                    inp=''
                    try:
                        inp=raw_input('\n\033[0m[\033[41;77;1m Masukan Opsi \033[0m] ').strip()
                    except:
                            print
                            exit(1)
                    if inp.strip().lower().find('quit')!=-1 or inp.strip().lower().find('exit')!=-1:
                            print
                            exit(1)
                    elif inp.strip() == "":
                            if not getState():
                                    break
                    elif inp.strip().lower().find("play") != -1:
                            try:
                                    k=int(inp[5:len(inp)])-1
                                    if k>=len(p) or k<0:
                                            print 'Maaf tidak bisa memainkan lagu yang kamu punya saja\n'+str(len(p))+'judul'
                                            print 'Pilih antara 1 sampai'+str(len(p))+'judul'
                                    else:
                                            n=k
                                            fg=False
                                            ref=True
                                            break
                            except:
                                    os.system('clear')
                                    os.system('reset')
                                    sleep(1)
                                    print
                                    print logo
                                    print example
                                    print
                                    print '\033[0mFrom \033[91;2m/storage/sdcard/'
                                    print '\033[0mSedang mendengarkan (memutar) \033[96;2mmusik Anda...\033[0m'
                                    print
                                    print "\033[77;4;1mTekan Ctrl + C untuk kembali\033[0m"
                                    print
                                    subprocess.call(["mpv \""+p[pos]+"\""],shell=True)
                                    exit(1)
                    elif inp.lower().find('pause') !=-1:
                            subprocess.call(["mpv \""+p[pos]+"\""],shell=True)
                            restart(1)
                    elif inp.lower().find('next') !=-1:
                            n=n+1
                            fg=False
                            ref=True
                            break
                    elif inp.lower().find('prev') !=-1:
                            n=n-1
                            fg=False
                            ref=True
                            break
                    elif inp.lower().find('rand') !=-1:
                            n=randint(0,len(p)-1)
                            ref=True
                            break
                    elif inp.lower().find('reload') !=-1:
                            genlist()
                            dislist()
                            n=randint(0,len(p)-1)
                            ref=True
                            break
                    elif inp.lower().find('sort') !=-1:
                            nsg=p[n]
                            sortlist()
                            n=p.index(nsg)
                            n=randint(0,len(p)-1)
                            ref=True
                            break
                    elif inp.lower().strip().find('remove') !=-1:
                            try:
                                    r=int(inp[7:len(inp)])-1
                                    remove(r)
                                    if n==r:
                                            subprocess.call(["mpv \""+p[pos]+"\""],shell=True)
                                            n=randint(0,len(p)-1)
                                    else:
                                            if pos>r:
                                                    pos=pos-1
                                                    n=pos
                                    ref=True
                                    break
                            except:
                                    print "\033[0m[\033[91;1m!\033[0m] Masukan dengan benar"
                    elif inp.lower().find('ref') !=-1:
                            cols=int(os.popen('echo $COLUMNS').read().split('\n')[0])
                            for pr in range(len(p)):
                                    l=p[pr].rfind('/')+1
                                    if l==0:
                                            continue
                                    ap=p[pr][l:len(p[pr])-4]
                                    dif=len(ap)-cols+30
                                    if dif>0:
                                            ap=ap[:len(ap)-dif]
                                    sname[pr]=ap
                            ref=True
                            break
                    elif inp.lower().find('.info') !=-1:
                            subprocess.call('termux-media-player > .info',shell=True)
                            f1=open(".info","r")
                            print(f1.read())
                            f1.close()
                    elif inp.lower().find('help') !=-1:
                            print
                            print """
Usage: termux-media-player cmd [args]

 help         Shows this help
 info        Displays current playback information
 play         Resumes playback if paused
 play <file>  Plays specified media file
 pause        Pauses playback
 stop         Quits playback """
                            print
                    else:
                            print "\n\033[0m[\033[91;1m!\033[0m] Masukan dengan benar\n"
                            sleep(1)
                            if not getState():
                                    break
            if  n >= len(p):
                    n=0
            elif n<0:
                    n=len(p)-1
            if ref and getState():
                    continue
            if getState()==False and fg:
                    n=n+1
                    if  n >= len(p):
                            n=0
                    elif n<0:
                            n=len(p)-1
    elif option.strip() in '2 ganti'.split():
        write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
        sleep(1)
        os.system('clear')
        os.system('reset')
        sleep(1)
        print
        print logo
        print example
        try:
            write("\n\033[0m[ \033[32mINFO \033[0m] \033[3mGunakan headset (earphone) biar lebih kennceeeng")
            write("         Sediakan kopi, roko + cemilan biar lebih mantaps\033[0m\n\n")
            u = raw_input('\033[0m[\033[103;90;1m Alur   \033[0m] ')
            i = raw_input('\033[0m[\033[101;77;1m Folder \033[0m] ')
            o = raw_input('\033[0m[\033[102;90;1m Album  \033[0m] ')
            x = raw_input('\033[0m[\033[104;77;1m Judul  \033[0m] ')
            print
            loads()
            sleep(3)
            os.system('clear')
            os.system('reset')
            sleep(1)
            print
            print logo
            print example
            print
            print '\033[0mFrom \033[91;2m/storage/'+u+'/'
            print '\033[0mSedang mendengarkan (memutar) \033[96;2mmusik Anda...'
            print
            print '\033[0m[\033[92;1m*\033[0m] Folder : '+i
            print '\033[0m[\033[94;1m#\033[0m] Album  : '+o
            print '\033[0m[\033[93;1m&\033[0m] Judul  : '+x
            print
            print "\033[77;4;1mTekan Ctrl + C untuk kembali\033[0m"
            print
            subprocess.call(['mpv /storage/'+u+'/'+i+'/'+o+'/'+x],shell=True)
            restart()
        except KeyboardInterrupt:
            print
            print
            print "\033[0m[\033[91;1m!\033[0m] \033[77;1mKembali\033[0m"
            print
            sleep(1)
            restart()
    elif option.strip() in '3 musik vidio'.split():
        write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
        sleep(1)
        os.system('clear')
        os.system('reset')
        sleep(1)
        print
        print logo
        print example
        print
        write("\033[0m[ \033[32mINFO \033[0m] \033[3mGunakan headset (earphone) biar lebih kennceeeng")
        write("         Sediakan kopi, roko + cemilan biar lebih mantaps\033[0m\n\n")
        o = raw_input('\033[0m[\033[95;1m?\033[0m] Cari vidio / musik: \033[77;1m')
        print
        loads()
        print
        os.system('python sch.py '+o)
        sleep(1)
        x = raw_input('\n\033[0m[\033[104;77;1m Tempel  \033[0m] ')
        write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
        sleep(3)
        try:
            os.system('clear')
            os.system('reset')
            sleep(1)
            print
            print logo
            print example
            print
            print '\033[0mFrom \033[91;2m/storage/sdcard/self/'
            print '\033[0mSedang mendengarkan (memutar) \033[96;2mmusik Anda...\033[0m'
            print
            print "\033[77;4;1mTekan Ctrl + C untuk kembali\033[0m"
            print
            subprocess.call(['mpv '+x],shell=True)
            restart()
        except KeyboardInterrupt:
            print
            print
            print "\033[0m[\033[91;1m!\033[0m] \033[77;1mKembali\033[0m"
            print
            sleep(1)
            menu()
    elif option.strip() in '4 downloads'.split():
        write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m\n")
        sleep(1)
        os.system('xdg-open https://m.youtube.com')
        os.system('clear')
        os.system('lolcat /storage/A892-D352/Termux/usr/libexec/zlib.exe-nedi1.txt')
        print
        sleep(5)
        restart()
    elif option.strip() in '& 3 lisensi'.split():
        print
        os.system('nano LICENSE')
        print
        restart()
    elif option.strip() in '# 4 info'.split():
        os.system('clear')
        print example
        os.system('toilet -f smslant Music')
        print info
        sleep(1)
        print
        raw_input('[ Tekan Enter ]')
        restart()
    elif option.strip() in '* 5 perbarui'.split():
        print
        os.system('git pull origin master')
        print
        raw_input('\033[0m[ \033[32mTekan Enter \033[0m]')
        restart()
    elif option.strip() in '- 0 keluar'.split():
        print "\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!"
        print
        sys.exit(1)
    else:
        print "\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]"
        print
        sleep(1)
        restart()

if __name__=='__main__':
        menu()
