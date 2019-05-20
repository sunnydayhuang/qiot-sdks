import time
import os
import random
import json
from lib import qiot
"""
	This sample code demo receive value from QIoT Suite Lite by HTTP protocol
	requirement:
	-- opkg update
	-- opkg install distribute
	-- opkg install python-openssl
	-- easy_install pip
	-- pip install requests
	run command: python http_get.py
"""

"""
	Setup connection options
"""
connection = qiot.connection(qiot.protocol.HTTP)
connection_options = connection.read_resource('./res/resourceinfo.json')

"""
	Receive data of QIoT Suite Lite.
"""
def on_message(event_trigger,data):
	message =json.loads(data["message"])
	if(data['id']=='temp'):
		print "temp : " + str(message['value'])
		print "------------------------"

connection.on("message",on_message)

while 1:
	connection.subscribe_by_id("temp")
	time.sleep(1)