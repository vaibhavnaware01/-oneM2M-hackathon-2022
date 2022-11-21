#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
import socket
import time
import socket
import requests
 
UDP_IP01=  "fd12:3456::5232:5fff:fe42:61c6"  #Smart Pole WN-LP01-03
UDP_IP02 = "fd12:3456::b6e3:f9ff:fea6:2e7"  #Vindya A2  WN-LP02-02
UDP_IP03=  "fd12:3456::5232:5fff:fe42:8a37" #Vindya A2-A4 WN-LP03-02
UDP_IP04 = "fd12:3456::b6e3:f9ff:fea6:314"  #Vindya A4  WN-LP04-02
UDP_IP05 = "fd12:3456::b6e3:f9ff:fea6:53e"  #Vindya A6  WN-LP05-02
UDP_IP06=  "fd12:3456::5232:5fff:fe42:5ea0" #pole 26    WN-LP06-01
UDP_IP07=  "fd12:3456::5232:5fff:fe42:5df9" #pole 25    WN-LP07-01
UDP_IP08=  "fd12:3456::5232:5fff:fe42:5e26" #pole 22    WN-LP08-01
UDP_IP09=  "fd12:3456::5232:5fff:fe42:6155" #pole 21    WN-LP09-01
UDP_IP10=  "fd12:3456::5232:5fff:fe42:61b0" #pole 20    WN-LP10-01
UDP_IP11=  "fd12:3456::5232:5fff:fe42:6039" #pole 19    WN-LP11-01
UDP_IP12=  "fd12:3456::5232:5fff:fe42:5dd8" #pole 18    WN-LP12-01
UDP_IP13=  "fd12:3456::5232:5fff:fe42:619d" #pole 66    WN-LP13-01
UDP_IP14=  "fd12:3456::5232:5fff:fe42:614d" #pole 65    WN-LP14-01
UDP_IP15=  "fd12:3456::5232:5fff:fe42:6177" #pole 64    WN-LP15-01
UDP_IP16=  "fd12:3456::5232:5fff:fe42:6160" #pole 63    WN-LP16-01
UDP_IP17=  "fd12:3456::5232:5fff:fe42:6154" #pole 62    WN-LP17-01
UDP_IP18=  "fd12:3456::5232:5fff:fe42:5dd8" #pole 61    WN-LP18-01
UDP_IP19=  "fd12:3456::5232:5fff:fe42:61d0" #pole 60    WN-LP19-01
UDP_IP20=  "fd12:3456::5232:5fff:fe42:61c9" #pole 59    WN-LP20-01
UDP_IP21=  "fd12:3456::5232:5fff:fe42:61d2" #pole 67    WN-LP21-01
UDP_IP22=  "fd12:3456::5232:5fff:fe42:5e8e" #pole 78    WN-LP22-01
UDP_IP23=  "fd12:3456::5232:5fff:fe42:5e01" #pole 77    WN-LP23-01
UDP_IP24=  "fd12:3456::5232:5fff:fe42:6168" #pole 80    WN-LP24-01
UDP_IP25=  "fd12:3456::5232:5fff:fe42:60ac" #pole 81    WN-LP25-01
UDP_IP26=  "fd12:3456::5232:5fff:fe42:61cf" #pole 82    WN-LP26-01
UDP_IP27=  "fd12:3456::5232:5fff:fe42:5e2a" #pole 83    WN-LP27-01
UDP_IP28=  "fd12:3456::5232:5fff:fe42:61ef" #pole 84    WN-LP28-01
UDP_IP29=  "fd12:3456::5232:5fff:fe42:607c" #pole 58    WN-LP29-01
UDP_IP30=  "fd12:3456::5232:5fff:fe42:61c7" #pole 37    WN-LP30-01
UDP_IP31=  "fd12:3456::5232:5fff:fe42:618d" #mobile node    WN-LP31-01
 
 
UDP_PORT = 5001
HOST_IP="fd12:3456::1"
f=open("latency.txt","w")
class S(BaseHTTPRequestHandler):
    global f
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        received_data = json.loads (post_data)
        try:
            con_data=received_data["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"]
            print(con_data)
            MESSAGE=con_data
            print ("message:", MESSAGE) 
            message_bytes = str.encode(MESSAGE) 
            sock = socket.socket(socket.AF_INET6, # Internet
            socket.SOCK_DGRAM) # UDP
            if MESSAGE== ".LP01ON" or MESSAGE==".LP01OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP01, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp01'%(str(start),str("start")))
                print("Send To UDP_IP01")
            elif MESSAGE== ".LP02ON" or MESSAGE==".LP02OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP02, UDP_PORT))   
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp02'%(str(start),str("start")))
                print("Send To UDP_IP02")
            elif MESSAGE== ".LP03ON" or MESSAGE==".LP03OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP03, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp03'%(str(start),str("start")))
                print("Send To UDP_IP03")
            elif MESSAGE== ".LP04ON" or MESSAGE==".LP04OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP04, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp04'%(str(start),str("start")))
                print("Send To UDP_IP04")
            elif MESSAGE== ".LP05ON" or MESSAGE==".LP05OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP05, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp05'%(str(start),str("start")))
                print("Send To UDP_IP05")
            elif MESSAGE== ".LP06ON" or MESSAGE==".LP06OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP06, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp06'%(str(start),str("start")))
                print("Send To UDP_IP06")
            elif MESSAGE== ".LP07ON" or MESSAGE==".LP07OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP07, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp07'%(str(start),str("start")))
                print("Send To UDP_IP07")
            elif MESSAGE== ".LP08ON" or MESSAGE==".LP08OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP08, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp08'%(str(start),str("start")))
                print("Send To UDP_IP08")
            elif MESSAGE== ".LP09ON" or MESSAGE==".LP09OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP09, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp09'%(str(start),str("start")))
                print("Send To UDP_IP09")
            elif MESSAGE== ".LP10ON" or MESSAGE==".LP10OFF":
                print("Send To UDP_IP10")
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP10, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp10'%(str(start),str("start")))
            elif MESSAGE== ".LP11ON" or MESSAGE==".LP11OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP11, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp11'%(str(start),str("start")))
                print("Send To UDP_IP11")
            elif MESSAGE== ".LP12ON" or MESSAGE==".LP12OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP12, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp12'%(str(start),str("start")))
                print("Send To UDP_IP12")
            elif MESSAGE== ".LP13ON" or MESSAGE==".LP13OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP13, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp13'%(str(start),str("start")))
                print("Send To UDP_IP13")
            elif MESSAGE== ".LP14ON" or MESSAGE==".LP14OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP14, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp14'%(str(start),str("start")))
                print("Send To UDP_IP14")
            elif MESSAGE== ".LP15ON" or MESSAGE==".LP15OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP15, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp15'%(str(start),str("start")))
                print("Send To UDP_IP15")
            elif MESSAGE== ".LP16ON" or MESSAGE==".LP16OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP16, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp16'%(str(start),str("start")))
                print("Send To UDP_IP16")
            elif MESSAGE== ".LP17ON" or MESSAGE==".LP17OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP17, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp17'%(str(start),str("start")))
                print("Send To UDP_IP17")
            elif MESSAGE== ".LP18ON" or MESSAGE==".LP18OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP18, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp18'%(str(start),str("start")))
                print("Send To UDP_IP18")
            elif MESSAGE== ".LP19ON" or MESSAGE==".LP19OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP19, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp19'%(str(start),str("start")))
                print("Send To UDP_IP19")
            elif MESSAGE== ".LP20ON" or MESSAGE==".LP20OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP20, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp20'%(str(start),str("start")))
                print("Send To UDP_IP20")
            elif MESSAGE== ".LP21ON" or MESSAGE==".LP21OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP21, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp21'%(str(start),str("start")))
                print("Send To UDP_IP21")
            elif MESSAGE== ".LP22ON" or MESSAGE==".LP22OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP22, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp22'%(str(start),str("start")))
                print("Send To UDP_IP22")
            elif MESSAGE== ".LP23ON" or MESSAGE==".LP23OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP23, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp23'%(str(start),str("start")))
                print("Send To UDP_IP23")
            elif MESSAGE== ".LP24ON" or MESSAGE==".LP24OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP24, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp24'%(str(start),str("start")))
                print("Send To UDP_IP24")
            elif MESSAGE== ".LP25ON" or MESSAGE==".LP25OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP25, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp25'%(str(start),str("start")))
                print("Send To UDP_IP25")
            elif MESSAGE== ".LP26ON" or MESSAGE==".LP26OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP26, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp26'%(str(start),str("start")))
                print("Send To UDP_IP26")
            elif MESSAGE== ".LP27ON" or MESSAGE==".LP27OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP27, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp27'%(str(start),str("start")))
                print("Send To UDP_IP27")
            elif MESSAGE== ".LP28ON" or MESSAGE==".LP28OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP28, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp28'%(str(start),str("start")))
                print("Send To UDP_IP28")
            elif MESSAGE== ".LP29ON" or MESSAGE==".LP29OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP29, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp29'%(str(start),str("start")))
                print("Send To UDP_IP29")
            elif MESSAGE== ".LP30ON" or MESSAGE==".LP30OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP30, UDP_PORT))
                x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp30'%(str(start),str("start")))
                print("Send To UDP_IP30")
            elif MESSAGE== ".LP31ON" or MESSAGE==".LP31OFF":
                start = str(time.time())
                sock.sendto(message_bytes, (UDP_IP31, UDP_PORT))
                print("Send To UDP_IP31")
            elif MESSAGE==".LP02STS" or MESSAGE==".LP02CHK":
                sock.sendto(message_bytes, (UDP_IP02, UDP_PORT))   
                print("Send To UDP_IP02")
            elif MESSAGE==".LP03STS" or MESSAGE==".LP03CHK":
                sock.sendto(message_bytes, (UDP_IP03, UDP_PORT))
                print("Send To UDP_IP03")
            elif MESSAGE==".LP04STS" or MESSAGE==".LP04CHK":
                sock.sendto(message_bytes, (UDP_IP04, UDP_PORT))
                print("Send To UDP_IP04")
            elif MESSAGE==".LP05STS" or MESSAGE==".LP05CHK":
                sock.sendto(message_bytes, (UDP_IP05, UDP_PORT))
                print("Send To UDP_IP05")
            elif MESSAGE==".LP06STS" or MESSAGE==".LP06CHK":
                sock.sendto(message_bytes, (UDP_IP06, UDP_PORT))
                print("Send To UDP_IP06")
            elif MESSAGE==".LP07STS" or MESSAGE==".LP07CHK":
                sock.sendto(message_bytes, (UDP_IP07, UDP_PORT))
                print("Send To UDP_IP07")
            elif MESSAGE==".LP08STS" or MESSAGE==".LP08CHK":
                sock.sendto(message_bytes, (UDP_IP08, UDP_PORT))
                print("Send To UDP_IP08")
            elif MESSAGE==".LP09STS" or MESSAGE==".LP09CHK":
                sock.sendto(message_bytes, (UDP_IP09, UDP_PORT))
                print("Send To UDP_IP09")
            elif MESSAGE==".LP10STS" or MESSAGE==".LP10CHK":
                print("Send To UDP_IP10")
                sock.sendto(message_bytes, (UDP_IP10, UDP_PORT))
            elif MESSAGE==".LP11STS" or MESSAGE==".LP11CHK":
                sock.sendto(message_bytes, (UDP_IP11, UDP_PORT))
                print("Send To UDP_IP11")
            elif MESSAGE==".LP12STS" or MESSAGE==".LP12CHK":
                sock.sendto(message_bytes, (UDP_IP12, UDP_PORT))
                print("Send To UDP_IP12")
            elif MESSAGE==".LP13STS" or MESSAGE==".LP13CHK":
                sock.sendto(message_bytes, (UDP_IP13, UDP_PORT))
                print("Send To UDP_IP13")
            elif MESSAGE==".LP14STS" or MESSAGE==".LP14CHK":
                sock.sendto(message_bytes, (UDP_IP14, UDP_PORT))
                print("Send To UDP_IP14")
            elif MESSAGE==".LP15STS" or MESSAGE==".LP15CHK":
                sock.sendto(message_bytes, (UDP_IP15, UDP_PORT))
                print("Send To UDP_IP15")
            elif MESSAGE==".LP16STS" or MESSAGE==".LP16CHK":
                sock.sendto(message_bytes, (UDP_IP16, UDP_PORT))
                print("Send To UDP_IP16")
            elif MESSAGE==".LP17STS" or MESSAGE==".LP17CHK":
                sock.sendto(message_bytes, (UDP_IP17, UDP_PORT))
                print("Send To UDP_IP17")
            elif MESSAGE==".LP18STS" or MESSAGE==".LP18CHK":
                sock.sendto(message_bytes, (UDP_IP18, UDP_PORT))
                print("Send To UDP_IP18")
            elif MESSAGE==".LP19STS" or MESSAGE==".LP19CHK":
                sock.sendto(message_bytes, (UDP_IP19, UDP_PORT))
                print("Send To UDP_IP19")
            elif MESSAGE==".LP20STS" or MESSAGE==".LP20CHK":
                sock.sendto(message_bytes, (UDP_IP20, UDP_PORT))
                print("Send To UDP_IP20")
            elif MESSAGE==".LP21STS" or MESSAGE==".LP21CHK":
                sock.sendto(message_bytes, (UDP_IP21, UDP_PORT))
                print("Send To UDP_IP21")
            elif MESSAGE==".LP22STS" or MESSAGE==".LP22CHK":
                sock.sendto(message_bytes, (UDP_IP22, UDP_PORT))
                print("Send To UDP_IP22")
            elif MESSAGE==".LP23STS" or MESSAGE==".LP23CHK":
                sock.sendto(message_bytes, (UDP_IP23, UDP_PORT))
                print("Send To UDP_IP23")
            elif MESSAGE==".LP24STS" or MESSAGE==".LP24CHK":
                sock.sendto(message_bytes, (UDP_IP24, UDP_PORT))
                print("Send To UDP_IP24")
            elif MESSAGE==".LP25STS" or MESSAGE==".LP25CHK":
                sock.sendto(message_bytes, (UDP_IP25, UDP_PORT))
                print("Send To UDP_IP25")
            elif MESSAGE==".LP26STS" or MESSAGE==".LP26CHK":
                sock.sendto(message_bytes, (UDP_IP26, UDP_PORT))
                print("Send To UDP_IP26")
            elif MESSAGE==".LP27STS" or MESSAGE==".LP27CHK":
                sock.sendto(message_bytes, (UDP_IP27, UDP_PORT))
                print("Send To UDP_IP27")
            elif MESSAGE==".LP28STS" or MESSAGE==".LP28CHK":
                sock.sendto(message_bytes, (UDP_IP28, UDP_PORT))
                print("Send To UDP_IP28")
            elif MESSAGE==".LP29STS" or MESSAGE==".LP29CHK":
                sock.sendto(message_bytes, (UDP_IP29, UDP_PORT))
                print("Send To UDP_IP29")
            elif MESSAGE==".LP30STS" or MESSAGE==".LP30CHK":
                sock.sendto(message_bytes, (UDP_IP30, UDP_PORT))
                print("Send To UDP_IP30")
            elif MESSAGE==".LP31STS" or MESSAGE==".LP31CHK":
                sock.sendto(message_bytes, (UDP_IP31, UDP_PORT))
                print("Send To UDP_IP31")
            self._set_response()
        except:
            self._set_response()
            self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
def run(server_class=HTTPServer, handler_class=S, port=1400):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')
 
if __name__ == '__main__':
    from sys import argv
 
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
