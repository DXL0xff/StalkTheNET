import os
import argparse
from shodan import Shodan

# this file will later be used to update StalkTheNET

# user API key from shodan.io
api_key = Shodan('YOUR API KEY')

total_ipcam = api_key.count('IP Webcam Server 0.4 HTTP/1.1 200 OK')
print('pullify -> \033[0;32m{}\033[0;m devices match string: \"IP Webcam Server 0.4 HTTP/1.1 200 OK\"'.format(total_ipcam['total']))

# shodan download IP_sever_04data "IP Webcam Server 0.4 HTTP/1.1 200 OK"
# shodan parse --fields ip_str,port --separator : IP_sever_04data.json.gz | sed 's/:$//' > IP_serv04_sed.txt

