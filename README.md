# Dynamic HTTP IP Webcam retriever and remote viewer

**PREFACE: _This tool can be used for malicious purposes and the developers are not liable for any misuse or legal actions against the end user_**

**Overview: StalkTheNET.py**

StalkTheNET is a python tool that is capable of using shodan queries to pull and parse remote IP Webcam hosts across the internet. StalkTheNET uses OpenCV to relay the HTTP request of http://target_address:port/shot.jpg in increments to mimick a real time web stream of the target IP Webcam. This tool target's IP Webcam Server's 0.2 through 0.4 and actively searches for an HTTP/1.1 200 OK callback
