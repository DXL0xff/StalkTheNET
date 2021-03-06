# Dynamic HTTP IP Webcam Retriever and Remote Viewer

**PREFACE: _This tool can be used for malicious purposes and the developers are not liable for any misuse or legal actions against the end user_**

**Overview:**

[StalkTheNET](https://github.com/DXL0xff/StalkTheNET/blob/master/stalkthenet.py) is a python tool that is capable of using [Shodan](https://www.shodan.io) queries to pull and parse remote IP Webcam hosts across the internet. [StalkTheNET](https://github.com/DXL0xff/StalkTheNET/blob/master/stalkthenet.py) uses [OpenCV](https://opencv.org/) and [Urllib](https://docs.python.org/3/library/urllib.html) to relay the HTTP request of **_http://target_address:port/shot.jpg_** in increments to mimick a real time web stream of the target IP Webcam. The tool `installer.py` file target's IP Webcam Server's 0.2 through 0.4 and actively searches for an HTTP/1.1 200 OK callback. Once the callback is retrieved `installer.py` parses the output to a whitelist or blacklist file to be used with `stalkthenet.py`

- `installer.py` actively send's HTTP queries to the external URL **_http://target_address:port/shot.jpg_** to verify if the resource from the remote host will be accessible for further interaction.
- `stalkthenet.py` requires the end user to supply a target URL that can either be chosen from `ipcam_whitelist.txt` or from an external source. If `stalkthenet.py` can open a connection to the target address, it will begin the HTTP relay through [OpenCV](https://opencv.org/) as long as a SIGINT is not sent to the end process by the user

**Requirements:**
_All of the following modules are for Python3 only_
1. [OpenCV](https://opencv.org/) or `sudo apt-get install python3-opencv`
1. [Urllib](https://docs.python.org/3/library/urllib.html) or `pip3 install urllib` 
1. [Numpy](http://www.numpy.org/) or `pip3 install numpy`
1. [Requests](http://docs.python-requests.org/en/master/) or `pip3 install requests`

**Installation:**
1. `cd $HOME/Documents/ && git clone https://github.com/DXL0xff/StalkTheNET.git`
1. `cd StalkTheNET/`
1. `python3 installer.py -make` 
   1. **Note: This operation may take some time depending on the end users upload and download speeds**
   1. This step will be used to create `ipcam_whitelist.txt` & `ipcam_blacklist.txt` files for `stalkthenet.py`
1. `python3 stalkthenet.py --host http://<target_address:port>` 
   1. **The <target_address:port> can be obtained from "ipcam_whitelist.txt"**

_THE `IP_serv02_sed.txt`, `IP_serv03_sed.txt`, `IP_serv04_sed.txt` FILES PRECONTAIN REMOTE HOST INFORMATION FOR YOU. SEE BELOW ON HOW TO UPDATE_

**Automatic IP Webcam Server 0.2-0.4 update with `installer.py`:**
1. `python3 --installer.py -make`
   1. Use this step if you do not have `ipcam_whitelist.txt` & `ipcam_blacklist.txt` in your current working directory
   
The following method listed below is for replacing the target hosts with updated information from refreshed [Shodan](https://www.shodan.io) queries, this process will be used in conjunction with `installer.py` which is used to separate the remote hosts into `ipcam_whitelist.txt` or `ipcam_blacklist.txt` files respectively, only use target information from `ipcam_whitelist.txt` with `stalkthenet.py`, avoid using and disregard the information from `ipcam_blacklist.txt`

**Manual IP Webcam Server 0.2-0.4 update:**
_You will need a Shodan account to continue_
1. `shodan init <API_KEY>`
1. `shodan download IP_sever_02data "IP Webcam Server 0.2 HTTP/1.1 200 OK"`
1. `shodan download IP_sever_03data "IP Webcam Server 0.3 HTTP/1.1 200 OK"`
1. `shodan download IP_sever_04data "IP Webcam Server 0.4 HTTP/1.1 200 OK"`
1. `shodan parse --fields ip_str,port --separator : IP_sever_02data.json.gz | sed 's/:$//' > IP_serv02_sed.txt`
1. `shodan parse --fields ip_str,port --separator : IP_sever_03data.json.gz | sed 's/:$//' > IP_serv03_sed.txt`
1. `shodan parse --fields ip_str,port --separator : IP_sever_04data.json.gz | sed 's/:$//' > IP_serv04_sed.txt`
1. `rm ipcam_* && python3 installer.py -make`

_INFO: Future updates for StalkTheNET will be available in the near future #Secure2019_
_StalkTheNET will eventually merge into the GlobalWatch framework, and be formatted to work as a plugin, along with other methods for interacting with open remote IP Webcam hosts across the internet such as [Yawcam](https://www.yawcam.com)_
