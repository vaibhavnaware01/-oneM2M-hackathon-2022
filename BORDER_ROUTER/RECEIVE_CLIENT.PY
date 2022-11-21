import socket
import time
import requests
HOST_IP="fd12:3456::1"
PORT = 5005
import socket
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
        'X-M2M-Origin': 'WisunMon@20:5T&6OnuL1iZ',
        'Content-type': 'application/{};ty=4'.format(data_format)}
 
    body = {
        "m2m:cin": {
            "con": "{}".format(value),
            "lbl": cin_labels,
            "cnf": "text"
        }
    }
 
    try:
        response = requests.post(uri_cnt, json=body, headers=headers)
    except TypeError:
        response = requests.post(uri_cnt, data=json.dumps(body), headers=headers)
    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))
def create_cindev(uri_cnt, value, cin_labels="", data_format="json"):
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
        'X-M2M-Origin': 'devtest:devtest',
        'Content-type': 'application/{};ty=4'.format(data_format)}
 
    body = {
        "m2m:cin": {
            "con": "{}".format(value),
            "lbl": cin_labels,
            "cnf": "text"
        }
    }
 
    try:
        response = requests.post(uri_cnt, json=body, headers=headers)
    except TypeError:
        response = requests.post(uri_cnt, data=json.dumps(body), headers=headers)
    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))
def telegram_bot_sendtext(bot_message):
    bot_token = '5425190445:AAGaIdWdvPeyNaf4SkYAKxMLKxDEu7FgliY'
    bot_chatID= '-1001503138173'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text=' + bot_message
    return requests.get(send_text)
    return respond.json
while True: 
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.bind((HOST_IP, PORT))
    data, addr = sock.recvfrom(2048) # buffer size is 2048 bytes
    data1= data.decode()
    print(data1)
    if data1 == "WN-LP01-03 is on" or data1=="WN-LP01-03 is off" :
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp01'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP01-03/Acknowledge",data1)
    elif data1== "WN-LP02-02 is on" or data1=="WN-LP02-02 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp02'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP02-02/Acknowledge",data1)
    elif data1== "WN-LP03-02 is on" or data1=="WN-LP03-02 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp03'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP03-02/Acknowledge",data1)
    elif data1== "WN-LP04-02 is on" or data1=="WN-LP04-02 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp04'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP04-02/Acknowledge",data1)
    elif data1== "WN-LP05-02 is on" or data1=="WN-LP05-02 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp05'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP05-02/Acknowledge",data1)
    elif data1== "WN-LP06-01 is on" or data1=="WN-LP06-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp06'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP06-01/Acknowledge",data1)
    elif data1== "WN-LP07-01 is on" or data1=="WN-LP07-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp07'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP07-01/Acknowledge",data1)
    elif data1== "WN-LP08-01 is on" or data1=="WN-LP08-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp08'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP08-01/Acknowledge",data1)
    elif data1== "WN-LP09-01 is on" or data1=="WN-LP09-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp09'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP09-01/Acknowledge",data1)
    elif data1== "WN-LP10-01 is on" or data1=="WN-LP10-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp10'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP10-01/Acknowledge",data1)
    elif data1== "WN-LP11-01 is on" or data1=="WN-LP11-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp11'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP11-01/Acknowledge",data1)
    elif data1== "WN-LP12-01 is on" or data1=="WN-LP12-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp12'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP12-01/Acknowledge",data1)
    elif data1== "WN-LP13-01 is on" or data1=="WN-LP13-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp13'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP13-01/Acknowledge",data1)
    elif data1== "WN-LP14-01 is on" or data1=="WN-LP14-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp14'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP14-01/Acknowledge",data1)
    elif data1== "WN-LP15-01 is on" or data1=="WN-LP15-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp15'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP15-01/Acknowledge",data1)
    elif data1 == "WN-LP16-01 is on" or data1=="WN-LP16-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp16'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP16-01/Acknowledge",data1)
    elif data1== "WN-LP17-01 is on" or data1=="WN-LP17-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp17'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP17-01/Acknowledge",data1)
    elif data1== "WN-LP18-01 is on" or data1=="WN-LP18-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp18'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP18-01/Acknowledge",data1)
    elif data1== "WN-LP19-01 is on" or data1=="WN-LP19-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp19'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP19-01/Acknowledge",data1)
    elif data1== "WN-LP20-01 is on" or data1=="WN-LP20-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp20'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP20-01/Acknowledge",data1)
    elif data1== "WN-LP21-01 is on" or data1=="WN-LP21-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp21'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP21-01/Acknowledge",data1)
    elif data1== "WN-LP22-01 is on" or data1=="WN-LP22-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp22'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP22-01/Acknowledge",data1)
    elif data1== "WN-LP23-01 is on" or data1=="WN-LP23-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp23'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP23-01/Acknowledge",data1)
    elif data1== "WN-LP24-01 is on" or data1=="WN-LP24-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp24'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP24-01/Acknowledge",data1)
    elif data1== "WN-LP25-01 is on" or data1=="WN-LP25-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp25'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP25-01/Acknowledge",data1)
    elif data1== "WN-LP26-01 is on" or data1=="WN-LP26-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp26'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP26-01/Acknowledge",data1)
    elif data1== "WN-LP27-01 is on" or data1=="WN-LP27-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp27'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP27-01/Acknowledge",data1)
    elif data1== "WN-LP28-01 is on" or data1=="WN-LP28-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp28'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP28-01/Acknowledge",data1)
    elif data1== "WN-LP29-01 is on" or data1=="WN-LP29-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp29'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP29-01/Acknowledge",data1)
    elif data1== "WN-LP30-01 is on" or data1=="WN-LP30-01 is off":
        end=str(time.time())
        x= requests.get('https://script.google.com/macros/s/AKfycbyyoRQEZavKD57gts6ZwYkl6pUorHYpuJh68DV74TX2o_UQ6qquOMOVEr5DCBpVQ7lO/exec?time=%s&category=%s&node_id=lp30'%(str(end),str("end")))
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP30-01/Acknowledge",data1)
    elif data1== "WN-LP31-01 is on" or data1=="WN-LP31-01 is off":
        end=str(time.time())
        create_cin ("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-LP30-01/Acknowledge",data1)
    create_cindev ("http://dev-onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WiSUN/Ack",data1)
    telegram_bot_sendtext(str(data1))
