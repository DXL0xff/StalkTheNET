# Dynamic HTTP IP Webcam Retriever and Remote Viewer

**PREFACE: _This tool can be used for malicious purposes and the developers are not liable for any misuse or legal actions against the end user_**

**Overview:**

[StalkTheNET](https://github.com/DXL0xff/StalkTheNET/blob/master/stalkthenet.py) is a python tool that is capable of using shodan queries to pull and parse remote IP Webcam hosts across the internet. [StalkTheNET](https://github.com/DXL0xff/StalkTheNET/blob/master/stalkthenet.py) uses [OpenCV](https://opencv.org/) and [Requests](http://docs.python-requests.org/en/master/) to relay the HTTP request of http://target_address:port/shot.jpg in increments to mimick a real time web stream of the target IP Webcam. The tool `installer.py` file target's IP Webcam Server's 0.2 through 0.4 and actively searches for an HTTP/1.1 200 OK callback. Once the callback is retrieved `installer.py` parses the output to a whitelist and blacklist file to be used with `stalkthenet.py`

- `installer.py` actively send's HTTP queries to the external URL _http://target_address:port/shot.jpg_ to verify if the resource from the remote host will be accessible for further interaction.
- `stalkthenet.py` requires the end user to supply a target URL that can either be chosen from `ipcam_whitelist.txt` or from an external source. If `stalkthenet.py` can open a connection to the target address, it will begin the HTTP relay through OpenCV as long as a SIGINT is not sent to the end process by the user

**Requirements:**
_All of the following modules are for Python3 only_
1. [OpenCV](https://opencv.org/) or `pip3 install cv2`
1. [Requests](http://docs.python-requests.org/en/master/) or `pip3 install requests` 
1. [Numpy](http://www.numpy.org/) or `pip3 install numpy`

**Installation:**
1. `cd $HOME && git clone https://github.com/DXL0xff/StalkTheNET.git`
1. `cd StalkTheNET/`
1. `python3 installer.py -make` **Note: This operation may take some time depending on the end users upload and download speeds**
1. `pythnon3 stalkthenet.py --host http://<target_address:port>` **The <target_address:port can be obtained from `ipcam_whitelist.txt`**

**Manual IP Webcam Server 0.2-0.4 update:**
_You will need a shodan account to continue_
1. `shodan init <API_KEY>`
1. `shodan download IP_sever_02data "IP Webcam Server 0.2 HTTP/1.1 200 OK"`
1. `shodan download IP_sever_03data "IP Webcam Server 0.3 HTTP/1.1 200 OK"`
1. `shodan download IP_sever_04data "IP Webcam Server 0.4 HTTP/1.1 200 OK"`
1. `shodan parse --fields ip_str,port --separator : IP_sever_02data.json.gz | sed 's/:$//' > IP_serv02_sed.txt`
1. `shodan parse --fields ip_str,port --separator : IP_sever_03data.json.gz | sed 's/:$//' > IP_serv03_sed.txt`
1. `shodan parse --fields ip_str,port --separator : IP_sever_04data.json.gz | sed 's/:$//' > IP_serv04_sed.txt`
1. `rm ipcam_*`
1. `python3 installer.py -make`

_INFO: Future updates for StalkTheNET will be available in the near future _
