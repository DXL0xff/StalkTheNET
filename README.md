# Dynamic HTTP IP Webcam retriever and remote viewer

**PREFACE: _This tool can be used for malicious purposes and the developers are not liable for any misuse or legal actions against the end user_**

**Overview:**

[StalkTheNET](https://github.com/DXL0xff/StalkTheNET/blob/master/stalkthenet.py) is a python tool that is capable of using shodan queries to pull and parse remote IP Webcam hosts across the internet. [StalkTheNET](https://github.com/DXL0xff/StalkTheNET/blob/master/stalkthenet.py) uses [OpenCV](https://opencv.org/) to relay the HTTP request of http://target_address:port/shot.jpg in increments to mimick a real time web stream of the target IP Webcam. This tool `installer.py` file target's IP Webcam Server's 0.2 through 0.4 and actively searches for an HTTP/1.1 200 OK callback. Once the callback is retrieved `installer.py` parses the output to a whitelist and blacklist file to be used with `stalkthenet.py`

- `installer.py` actively send HTTP queries to the external URL http://target_address:port/shot.jpg to verify if the resource from the remote host will be accessible for further interaction.
- `stalkthenet.py` requires the end user to supply a target URL that can either be chosen from `ipcam_whitelist.txt` or from an external source. If `stalkthenet.py` can open a connection to the target address, it will begin the HTTP relay through OpenCV as long as a SIGINT is not sent to the end process by the user

**Installation:**
1. `
