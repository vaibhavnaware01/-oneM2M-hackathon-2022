import re
import ast
import json
import requests
import time
import calendar
import sys
from datetime import datetime
from pprint import pprint as pprint
import gspread
current_GMT = time.gmtime()
ts = calendar.timegm(current_GMT)
from oauth2client.service_account import ServiceAccountCredentials
initial_node_row = 2
current_module = sys.modules[__name__]
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
node_ids=["WN-LP01-03","WN-LP02-02","WN-LP03-02","WN-LP04-02","WN-LP05-02","WN-LP06-01","WN-LP07-01","WN-LP08-01","WN-LP09-01","WN-LP10-01","WN-LP11-01","WN-LP12-01","WN-LP13-01","WN-LP14-01","WN-LP15-01"
          ,"WN-LP16-01","WN-LP17-01","WN-LP18-01","WN-LP19-01","WN-LP20-01","WN-LP21-01","WN-LP22-01","WN-LP23-01","WN-LP24-01","WN-LP25-01",
          "WN-LP26-01","WN-LP27-01","WN-LP28-01","WN-LP29-01","WN-LP30-01"]

UDP_IP01=  ("fd12:3456::5232:5fff:fe42:61c6" , "WN-LP01-03")
UDP_IP02=  ("fd12:3456::b6e3:f9ff:fea6:02e7" , "WN-LP02-02")
UDP_IP03=  ("fd12:3456::5232:5fff:fe42:8a37" , "WN-LP03-02")
UDP_IP04=  ("fd12:3456::b6e3:f9ff:fea6:0314" , "WN-LP04-02")
UDP_IP05=  ("fd12:3456::b6e3:f9ff:fea6:053e" , "WN-LP05-02")
UDP_IP06=  ("fd12:3456::5232:5fff:fe42:5ea0" , "WN-LP06-01")
UDP_IP07=  ("fd12:3456::5232:5fff:fe42:5df9" , "WN-LP07-01")
UDP_IP08=  ("fd12:3456::5232:5fff:fe42:5e26" , "WN-LP08-01")
UDP_IP09=  ("fd12:3456::5232:5fff:fe42:6155" , "WN-LP09-01")
UDP_IP10=  ("fd12:3456::5232:5fff:fe42:61b0" , "WN-LP10-01")
UDP_IP11=  ("fd12:3456::5232:5fff:fe42:6039" , "WN-LP11-01")
UDP_IP12=  ("fd12:3456::5232:5fff:fe42:5dd8" , "WN-LP12-01")
UDP_IP13=  ("fd12:3456::5232:5fff:fe42:619d" , "WN-LP13-01")
UDP_IP14=  ("fd12:3456::5232:5fff:fe42:614d" , "WN-LP14-01")
UDP_IP15=  ("fd12:3456::5232:5fff:fe42:6177" , "WN-LP15-01")
UDP_IP16=  ("fd12:3456::5232:5fff:fe42:6160" , "WN-LP16-01")
UDP_IP17=  ("fd12:3456::5232:5fff:fe42:6154" , "WN-LP17-01")
UDP_IP18=  ("fd12:3456::5232:5fff:fe42:5def" , "WN-LP18-01")
UDP_IP19=  ("fd12:3456::5232:5fff:fe42:61d0" , "WN-LP19-01")
UDP_IP20=  ("fd12:3456::5232:5fff:fe42:61c9" , "WN-LP20-01")
UDP_IP21=  ("fd12:3456::5232:5fff:fe42:61d2" , "WN-LP21-01")
UDP_IP22=  ("fd12:3456::5232:5fff:fe42:5e8e" , "WN-LP22-01")
UDP_IP23=  ("fd12:3456::5232:5fff:fe42:5e01" , "WN-LP23-01")
UDP_IP24=  ("fd12:3456::5232:5fff:fe42:6168" , "WN-LP24-01")
UDP_IP25=  ("fd12:3456::5232:5fff:fe42:60ac" , "WN-LP25-01")
UDP_IP26=  ("fd12:3456::5232:5fff:fe42:61cf" , "WN-LP26-01")
UDP_IP27=  ("fd12:3456::5232:5fff:fe42:5e2a" , "WN-LP27-01")
UDP_IP28=  ("fd12:3456::5232:5fff:fe42:61ef" , "WN-LP28-01")
UDP_IP29=  ("fd12:3456::5232:5fff:fe42:607c" , "WN-LP29-01")
UDP_IP30=  ("fd12:3456::5232:5fff:fe42:61c7" , "WN-LP30-01")

def gsheet_init():
    creds=ServiceAccountCredentials.from_json_keyfile_name(r"/home/pi/Desktop/abc/creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("WiSUNLatency").sheet1
    return sheet.get_all_values()

def get_rssi():
    f = open('/home/pi/wisun-br-linux/rssi_temp.txt','r+')
    data = f.read()
    result = re.findall(r"(Src.*rssi:-[0-9]{2})",data)
    final_list = []
    for item in result:
        for i in range(1,31):
            val = getattr(current_module, f'UDP_IP{str(i).zfill(2)}')
            if (val[0][-14:].replace(":","") == item[10:27:].replace(":","")):
                final_list.append([str(ts),"0",(item[-3::]),"50",val[0],"0",val[1]])
                #id = final_list[-1].pop()
    f.truncate(0)
    f.close()
    return final_list

def get_latency(node_id, latency_list):
    for i in range(2,16,5):
        try:
            latency_val = int(latency_list[i+2][latency_list[i-1].index(node_id)])
            return str(latency_val)
        except ValueError:
            pass
def create_cin(uri_cnt, value, cin_labels="", data_format="json"):
    """
        Method description:
        Deletes/Unregisters an application entity(AE) from the OneM2M framework/tree
        under the specified CSE
        Parameters:
        uri_cse : [str] URI of parent CSE
        ae_name : [str] name of the AE
        fmt_ex : [str] payload format
    """
    headers = {
        'X-M2M-Origin': 'guest:guest',
        'Content-type': 'application/{};ty=4'.format(data_format)}

    body = {
        "m2m:cin": {
            "con": "{}".format(value),
            "lbl": ["AE-WN",
                   "V1.0.0",
                   "AE-WN-V1.0.0"],
            "cnf": "text"
        }
    }
    
    try:
        response = requests.post(uri_cnt, json=body, headers=headers)
    except TypeError:
        response = requests.post(uri_cnt, data=json.dumps(body), headers=headers)
    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))
while True:
    if __name__ == '__main__':
        latency_list = gsheet_init()
        #get_latency("WN-LP28-01",latency_list)
        rssi_list = get_rssi()
        for data in rssi_list:
            ids = data.pop()
            data[1] = get_latency(ids,latency_list)
            pprint(data)
            data= ('[%s]' % ', '.join(map(str, data)))
            #data = str(data)[1:-1]
            print(data)
            create_cin (f"http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/{ids}/Data",data)
    time.sleep(300)
