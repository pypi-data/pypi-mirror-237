import websocket  # You can use either "python3 setup.py install" or "pip3 install websocket-client"

# to install this library.

try:
    import thread
except ImportError:
    import _thread as thread
import time



endpoint = "wss://nimblewebstream.lisuns.com:4576/"
apikey = "2dd48f71-f99d-4eab-9792-b06c9aa93795"
"""
endpoint = "ws://test.lisuns.com:4575/"
apikey = "c1850947-3b40-45ea-8f14-c79a812ad030"
"""

def Authenticate(ws):
    print("Authenticating...")
    ws.send('{"MessageType":"Authenticate","Password":"' + apikey + '"}')


def SubscribeRealtime(ws):
    Exchange = "NFO"  # GFDL : Supported Values: NFO, NSE, NSE_IDX, CDS, MCX. Mandatory Parameter
    InstIdentifier = "NIFTY-I"  # GFDL : String of symbol name : NIFTY-I, RELIANCE, NIFTY 50, NATURALGAS-I, USDINR-I
    Unsubscribe = "false"  # GFDL : To stop data subscription for this symbol, send this value as "true"
    strMessage = '{"MessageType":"SubscribeRealtime","Exchange":"' + Exchange + '","Unsubscribe":"' + Unsubscribe + '","InstrumentIdentifier":"' + InstIdentifier + '"}'
    print('Message : ' + strMessage)
    ws.send(strMessage)

def on_message(ws, message):
    print("Response : " + message)
    # Authenticate : {"Complete":true,"Message":"Welcome!","MessageType":"AuthenticateResult"}
    allures = message.split(',')
    strComplete = allures[0].split(':')
    result = str(strComplete[1])
    # print('Response : ' + result)
    if result == "true":
        print('AUTHENTICATED!!!')
        SubscribeRealtime(ws)  # GFDL : Subscribes to realtime data (server will push new data whenever available)

def on_error(ws, error):
    print("Error")


def on_close(ws):
    print("Reconnecting...")
    websocket.setdefaulttimeout(30)
    ws.connect(endpoint)


def on_open(ws):
    # print("Connected...")
    def run(*args):
        time.sleep(1)
        Authenticate(ws)

    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(endpoint,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()

"""
To connect using WebSockets API, you will need following information :
 
– “endpoint” to connect to
– “port number” to connect to
– “API Key” received from our team to access data
 
The flow of operations should be as follows :
 
1. Make a connection to the ws://endpoint:port
2. Send Authentication Request using API Key
3. Once authentication is successful, send all other data requests
4. If connection is lost for any reasons, follow same steps from 1 to 3 as above.

pip install gfdlws

import gfdlws as gw
import sys

con = gw.ws.connect(<EndPoint>, <API Key>)

Response
If key is authenticated server will send below response in JOSN format

{"Complete":true,"Message":"Welcome!","MessageType":"AuthenticateResult"}"

import gfdlws as gw
import sys

con = gw.ws.connect(<EndPoint>, <API Key>)
while True:
	time.sleep(1)
	response = gw.realtime.get(con,<Exchange>,<InstrumentIdentifier>, <Unsubscribe Optional [true]/[false][default=false]>)
	print(str(response))

import gfdlws as gw
import sys

con = gw.ws.connect(<EndPoint>, <API Key>)
while True:
    time.sleep(1)
    response = gw.realtime.get(con, 'NFO', 'NIFTY-I')
    print(str(response))


"""
