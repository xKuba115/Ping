import os
import datetime
import string
import re
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
i=0
x=0
ip1 = input (f"Input ID, if many, split with ',' \n")
ip1 = ip1.replace(" ","")
ip1=ip1.split(',')
ip_list = ip1
def check(adress):
    if(re.search(regex, adress)):
        return 1
    else:
        return 0
     

for ip in ip_list:
    if check(ip)==0:
        x=x+1

if x!=0:
    print(f"One of the adresses is invalid")
elif x==0:
    while True:
        i=0
        for ip in ip_list:

            file = open(f"{ip_list[i]} Ping.txt", 'a')
            response = os.popen(f"ping {ip}").read()
            now = datetime.datetime.now()
            if "Minimum =" in response:
                file.write(f"{ip} Ping Successful - {now} \n ")
            else:
                file.write(f"{ip} Ping Unsuccessful - {now} \n ")
                file.close()
            i=i+1