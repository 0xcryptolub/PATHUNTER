import urllib.request
import urllib.error
import pyfiglet
import time

banner = pyfiglet.figlet_format("PATHUNTER", font="digital")

print(banner, "\t\t\tby  Cracked Version")

print("<----------------------------------------->\n")

dirb=0
ip=input("[@]\tYour target url:\t")
file=input("[@]\tProvide wordlist:\t")
print("[-]\tStarted scanning  "+ip+"  at  "+time.asctime( time.localtime(time.time()) ))
print("[-]\tVersion 1.0    for updates-> https://github.com/0xcryptolub")
try:
    re_url=urllib.request.urlopen(ip)
except urllib.error.HTTPError as exp1:
    print(exp1.getcode())
except urllib.error.URLError as exp1:
    print(exp1.reason())
else:
    print("[!]\tHost status:\t"+str(re_url.getcode()))
    
wordlist=open(file,"r")
data = wordlist.read()
datainlist=data.split("\n")
print("[*]\tTotal payloads:\t"+str(len(datainlist)))
for i in range(0,len(datainlist)):
    dirb= ip+"/"+datainlist[i]
    #print(dirb)
    try:
        re_dirb=urllib.request.urlopen(dirb)
    except urllib.error.HTTPError as exp:
        print("[->]\t"+dirb+"    "+str(exp.getcode()))
    except urllib.error.URLError as exp:
        print(exp.reason())
    else:
        print("[->]\t"+dirb+"    "+str(re_dirb.getcode()))
