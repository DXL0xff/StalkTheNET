import os
import sys
import time
import argparse
import requests
import subprocess
import urllib.request

# python3 installer.py --make

'''
create whitelist and blacklist files
parse through all 3 data files, and test connection
separate all ip's into blacklist and whitelist files respectfully
'''

remote_webcams = []
target_files = ['IP_serv02_sed.txt', 'IP_serv03_sed.txt', 'IP_serv04_sed.txt']

def setup():
    # create blacklist and whitelist files
    if os.path.isfile(f'{os.getcwd()}/ipcam_whitelist.txt') and os.path.isfile(f'{os.getcwd()}/ipcam_blacklist.txt') == 1:
        pass

    else:
        print('installer.py => Creating \'ipcam_whitelist.txt\' & \'ipcam_blacklist.txt\' files...')
        time.sleep(2)
        os.system(f'touch {os.getcwd()}/ipcam_whitelist.txt ipcam_blacklist.txt')
        
        if os.path.isfile(f'{os.getcwd()}/ipcam_whitelist.txt') and os.path.isfile(f'{os.getcwd()}/ipcam_blacklist.txt') == 0:
            print('**req_serverhttp [ ERROR ] -> Failed to create \'ipcam_whitelist.txt\' & \'ipcam_blacklist.txt\'')
            sys.exit(-1)
        else:
            pass

def parse_data():
    for file in target_files:
        with open(f'{os.getcwd()}/{file}', 'r') as webcam_url:
            for remote_host in webcam_url:
                
                filter_target = remote_host.strip('\n')
                remote_webcams.append(filter_target)

host_count = 0

def separate_hosts():
    global host_count
    webcam_length = len(remote_webcams)

    for webcam_host in remote_webcams:
        format_string = f'http://{webcam_host}/shot.jpg'

        try:
            with urllib.request.urlopen(f'{format_string}') as response:
                ret_status = response.read()

        except Exception:
                print(f'**installer.py** [ INFO ] -> Connection refused -> \033[0;33m{format_string}\033[0;m. Skipping this host...')
                with open(f'{os.getcwd()}/ipcam_blacklist.txt', 'a') as blacklist_host:
                    blacklist_host.write(webcam_host+'\n')
                
                host_count += 1
                print(f'[ INFO ] -> Parsed \033[0;32m{host_count}\033[0;m out of \033[0;32m{webcam_length}\033[0;m remote webcams...')

        else:
                print(f'**installer.py** [ SUCCESS ] -> Target resource \033[0;32mhttp://{webcam_host}/shot.jpg\033[0;m is open..whitelisting host...')
                with open(f'{os.getcwd()}/ipcam_whitelist.txt', 'a') as whitelist_host:
                    whitelist_host.write(webcam_host+'\n')

                host_count += 1
                print(f'**installer.py** [ INFO ] -> Parsed \033[0;32m{host_count}\033[0;m out of \033[0;32m{webcam_length}\033[0;m remote webcams...')

    blacklist_host.close()
    whitelist_host.close()
    print('installer.py -> Remote host parser operation finished. Choose target from \'ipcam_whitelist.txt\' to use with stalkthenet.py')
    
    blacklist_count = subprocess.getoutput(f'wc -l {os.getcwd()}/ipcam_blacklist.txt')
    whitelist_count = subprocess.getoutput(f'wc -l {os.getcwd()}/ipcam_whitelist.txt')
    print(f'installer.py [ INFO ]-> \033[0;32m{whitelist_count}\033[0;m target hosts whitelisted : \033[0;33m{whitelist_count}\033[0;m remote hosts blacklisted')
    sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='installer.py', description='environment initializer script')

    parser.add_argument('--make', help='initialize and setup environment for StalkTheNET', action='store_true')
    args = parser.parse_args()

    if args.make:
        setup()
        parse_data()
        separate_hosts()