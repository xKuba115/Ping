import os
import datetime
import string
import re
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
i=0
ip1 = input ("Wprowadź IP")
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
        print(f"Adress {ip} is Invalid ")
    elif check(ip)==1:
            file = open(f"{ip_list[i]} Ping.txt", 'a')
            response = os.popen(f"ping {ip}").read()
            now = datetime.datetime.now()
            if "Minimum =" in response:
                file.write(f"{ip} Ping Successful - {now} \n ")
            else:
                file.write(f"{ip} Ping Unsuccessful - {now} \n ")
                file.close()
            i=i+1