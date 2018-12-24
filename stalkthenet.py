import sys
import cv2
import requests
import argparse
import subprocess
import numpy as np 
from datetime import datetime


# target url
# https limit rates requests to the same url
# can access from browser via https
# requests password when its http

def remote_view():
	target = f'{args.host}/shot.jpg'

	try:

		while True:

			d = datetime.now()

			fdesc = None
			
			img_resp = requests.get(target)
			img_array = np.array(bytearray(img_resp.content), dtype=np.uint8)

			# convert image array to cv2 image object
			image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
			# get the video feed to grayscale without api

			font = cv2.FONT_HERSHEY_SIMPLEX
			# object, text, placing, font, font-size, color, 
			cv2.putText(image, 'StalkTheNET v 0.2.1 %s %s %s:%s:%s' % (d.day, d.month, d.hour, d.minute, d.second), (0, 100), font, 1, (0,255,0), 2, cv2.LINE_AA)
			cv2.imshow(str('StalkTheNET Remote IPcam View -> ' + target), image)
		
			key = cv2.waitKey(1) & 0xFF
			remote_view()
		
		
	except KeyboardInterrupt:
		print('**[ \033[0;32mINFO\033[0;m ] StalkTheNET.py -> INFO: Ending remote TCP stream view. Shutting down..')
		sys.exit(1)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(prog='StalkTheNet', description='Remote IP Webcam Viewer')

	parser.add_argument('--host', help='the target address to connect to', required=True)
	args = parser.parse_args()

	if args.host:
		remote_view()





