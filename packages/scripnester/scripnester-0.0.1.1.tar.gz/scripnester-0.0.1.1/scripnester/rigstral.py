import pandas as pd
import numpy as np
import datetime as dt
import json
import time
import websocket  # You can use either "python3 setup.py install" or "pip3 install websocket-client"
from threading import Lock
from dhanhq import *
from enum import Enum
from midstral import *
try:
	import thread
except ImportError:
	import _thread as thread
# rigs 
class rigs:
	# class ticks
	
	class ticks:
		def trend(self):
			return list(self.f.up)
			pass
		def fastm(self):
			return list(self.f.tm03)
			pass
		def slotm(self):
			return list(self.f.tm12)
			pass
		def getdf(self):
		    	return self.f
		    	pass	
		def getindex(self):
		    	return self.f.index
		    	pass	
		def getavg(self):
		    	return self.f.avg
		    	pass
		def __init__(self,f,p):
			ohlc = {'Open':'first',
				'High':'max',
				'Low':'min',
				'Close':'last'}
			self.f = f.resample(p,offset='15min').apply(ohlc)
			self.f['avg']=(self.f.iloc[:,0:4]).mean(axis=1)
			def getsma(N):
	    			return (self.f.avg.rolling(N).mean()).fillna(0)
	    			pass
			def getema(s,N):
			    	k=2/(1+N)
			    	return s.ewm(alpha=k,adjust=False).mean()
			    	pass
			def gettma(s,N):
			    	k=2/(1+N)
			    	e1 = getema(s,N)
			    	e2 = getema(e1,N)
			    	e3 = getema(e2,N)
			    	return (3*e1) - (3*e2) + e3
			    	pass	
			self.f['tmoneto'] = gettma(self.f.avg,12)
			self.f['tmthree'] = gettma(self.f.avg,3)
			def vals():
				if(list(self.f.tmthree) > list(self.f.avg)):
					return True
				else:
					return False			
			self.f['up']=vals()
			pass
		pass
	"""

	# class ticks
	class ticks:
		def trend(self):
			return list(self.f.up)
			pass
	
		def fastm(self):
			return list(self.f.fasttm)
			pass
		
		def slotm(self):
			return list(self.f.slowtm)
			pass
			
		def getdf(self):
		    	return self.f
		    	pass	
		    
		def getindex(self):
		    	return self.f.index
		    	pass	
		    
		def getopen(self):
		    	return self.f.o
		    	pass	
		    
		def gethigh(self):
		    	return self.f.h
		    	pass	
		    
		def getlow(self):
		    	return self.f.l
		    	pass	
		    
		def getclose(self):
		    	return self.f.c
		    	pass	
		    
		def getavg(self):
		    	return self.f.avg
		    	pass
		pass
		
		def __init__(self,f,p):
			ohlc = {'Open':'first',
				'High':'max',
				'Low':'min',
				'Close':'last'}
			self.f = f.resample(p,offset='15min').apply(ohlc)
			self.f['avg']=(self.f.iloc[:,0:4]).mean(axis=1)
			
			self.f['c'] = self.f.avg.ewm(alpha=0.5,adjust=False).mean()
			self.f['o'] = (
					(
						self.f.Open.shift(1) + self.f.c.shift(1)
					)/2
				).ewm(alpha=0.5,adjust=False).mean()

			#t = np.maximum(self.f.High,self.f.o)
			self.f['h'] = (np.maximum(
						np.maximum(
							self.f.High,
							self.f.o
							),
							self.f.c
						)
					).ewm(alpha=0.5,adjust=False).mean()

			#t = np.minimum(self.f.Low,self.f.o)
			self.f['l'] = (np.minimum(
						np.minimum(
							self.f.Low,
							self.f.o
							),
							self.f.c
						)
					).ewm(alpha=0.5,adjust=False).mean()
			
			def getsma(N):
	    			return (self.f.avg.rolling(N).mean()).fillna(0)
	    			pass
	
			def getema(s,N):
			    	k=2/(1+N)
			    	return s.ewm(alpha=k,adjust=False).mean()
			    	pass
			
			def gettma(s,N):
			    	k=2/(1+N)
			    	e1 = getema(s,N)
			    	e2 = getema(e1,N)
			    	e3 = getema(e2,N)
			    	return (3*e1) - (3*e2) + e3
			    	pass	
									
			self.f['fasttm'] = gettma(self.f.avg,3)
			
			self.f['slowtm'] = gettma(self.f.avg,12)
			
			def vals():
				if(list(self.f.fasttm) > list(self.f.avg)):
					return True
				else:
					return False			
			
			self.f['up']=vals()
			#print(self.f.shape)
			pass
		pass
	"""
	# enum type nest fix
	class nest(Enum):
		me_	= '1101194979'
	
	class fix(Enum):
		one 	= '1Min'
		fiv 	= '5Min'
		ten 	= '10Min'
		pass
	"""
	def __new__(cls,s,secid,token):
			
		return instance(cls)	
		pass
	"""
	def __init__(self,s,secid,token):
		self.s=s
		self.endpoint=str((self.s.snaps()).endpoint.value)
		self.apikey=str((self.s.snaps()).apikey.value)
		self.brokey=str((self.s.snaps()).brokey.value)
		self.secid=str(secid)
		self.token=token
		self.dhn=self.s.enter(self.nest.me_.value,self.brokey)
		# initial structure of data 
		d=[{
			"Exchange":"NFO",
			"InstrumentIdentifier":"NIFTY-I",
			"LastTradeTime":1669262572,
			"ServerTime":1669262572,
			"AverageTradedPrice":18309.69,
			"BuyPrice":18323.9,
			"BuyQty":50,
			"Close":18286.75,
			"High":18329.35,
			"Low":18297.15,
			"LastTradePrice":18325.0,
			"LastTradeQty":750,
			"Open":18310.0,
			"OpenInterest":5657350,
			"QuotationLot":50.0,
			"SellPrice":18325.1,
			"SellQty":100,
			"TotalQtyTraded":681250,
			"Value":12473476312.5,
			"PreOpen":False,
			"PriceChange":38.25,
			"PriceChangePercentage":0.21,
			"OpenInterestChange":-98200,
			"MessageType":"RealtimeResult"
		}]
		# create structure for data 
		self.f=pd.DataFrame(d)
		self.f.set_index(pd.to_datetime(self.f.LastTradeTime.apply(lambda a:dt.datetime.fromtimestamp(a))),inplace=True)
		# self.u.logevent(str(self.f))
		# delte or dro the row
		self.f=self.f.drop(self.f.index[0])
		self.start=False
		self.lockbuy=Lock()
		self.locksel=Lock()
		print(self.f)
		pass
		
	def cru_z(self):
		# to install this library.
		
		def Authenticate(ws):
			#print('Authenticate   -----------------------------------------------------------------------------------------------')
			print("Authenticating...")
			ws.send('{"MessageType":"Authenticate","Password":"' + self.apikey + '"}')
			
		def SubscribeRealtime(ws):
			#print('SubscribeRealtime   -----------------------------------------------------------------------------------------------')
			Exchange = "NFO"  # GFDL : Supported Values: NFO, NSE, NSE_IDX, CDS, MCX. Mandatory Parameter
			InstIdentifier = self.token  # GFDL : String of symbol name : NIFTY-I, RELIANCE, NIFTY 50, NATURALGAS-I, USDINR-I
			Unsubscribe = "false"  # GFDL : To stop data subscription for this symbol, send this value as "true"
			strMessage = '{"MessageType":"SubscribeRealtime","Exchange":"' + Exchange + '","Unsubscribe":"' + Unsubscribe + '","InstrumentIdentifier":"' + InstIdentifier + '"}'
			#print('Message : ' + strMessage)
			ws.send(strMessage)
			
		def on_message(ws, message):
			#print('on_message   -----------------------------------------------------------------------------------------------')
			#print("Response : " + message)
			m=json.loads(message)
			#print('on_message   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
			if(m.get('MessageType')=='RealtimeResult'):
				self.f.loc[len(self.f)]=m
				self.f.set_index(pd.to_datetime(self.f.LastTradeTime.apply(lambda a:dt.datetime.fromtimestamp(a))),inplace=True)
			#print('on_message   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
			#print((self.f).shape)
			self.omnt=self.ticks(self.f.LastTradePrice,self.fix.one.value)
			print((self.omnt.getdf()).shape)
			self.fmnt=self.ticks(self.f.LastTradePrice,self.fix.fiv.value)
			print((self.fmnt.getdf()).shape)
			if (dt.time(9,15,00) < dt.datetime.now().time() < dt.time(15,30,00)):
				if((self.omnt.trend())[-1] == True and (self.fmnt.trend())[-1] == True): 
					if(self.lockbuy.locked()==False):
						self.lockbuy.acquire()
						self.s.logevent('buy fut')
						"""
						self.s.bye(self.dhn,
							self.secid,
							self.quantity,
							self.f.LastTradePrice
							)
						"""
						if(self.locksel.locked==True):
							self.locksel.release()
				if((self.omnt.trend())[-1] == False and (self.fmnt.trend())[-1] == False):
		     			if(self.locksel.locked()==False):
		     				self.locksel.acquire()
		     				self.s.logevent('sell fut')
		     				"""
		     				self.s.sel(self.dhn,
		     					self.secid,
		     					self.quantity,
		     					self.f.LastTradePrice
		     					)
		     				"""	
		     				if(self.lockbuy.locked()==True):
		     					self.lockbuy.release()	     					
							
			# Authenticate : {"Complete":true,"Message":"Welcome!","MessageType":"AuthenticateResult"}
			allures = message.split(',')
			strComplete = allures[0].split(':')
			result = str(strComplete[1])
			# print('Response : ' + result)
			if result == "true":
				print('AUTHENTICATED!!!')
				SubscribeRealtime(ws)  # GFDL : Subscribes to realtime data (server will push new data whenever available)

		def on_error(ws, error):
			#print('on_error   -----------------------------------------------------------------------------------------------')
			print("Error")

		def on_close(ws):
			#print('on_close   -----------------------------------------------------------------------------------------------')
			#print("Reconnecting...")
			websocket.setdefaulttimeout(30)
			ws.connect(self.endpoint)

		def on_open(ws):
			#print('on_open   -----------------------------------------------------------------------------------------------')
			#print("Connected...")
			def run(*args):
				time.sleep(1)
				Authenticate(ws)
			thread.start_new_thread(run, ())

		if __name__ == "__main__":
			print('__name__   -----------------------------------------------------------------------------------------------')
			websocket.enableTrace(True)
			ws = websocket.WebSocketApp(self.endpoint,
					on_open=on_open,
					on_message=on_message,
					on_error=on_error,
					on_close=on_close)
			ws.run_forever()
		else:
			print('__name__   -----------------------------------------------------------------------------------------------')
			websocket.enableTrace(False)
			ws = websocket.WebSocketApp(self.endpoint,
					on_open=on_open,
					on_message=on_message,
					on_error=on_error,
					on_close=on_close)
			ws.run_forever()	
		pass
		
	def getltp():
		return self.f.LastTradePrice
		pass
		
	def savetofile(self):
		if(dt.datetime.now().time() >= dt.time(15,30,00)):
			self.s.logevent('saving to file')
			self.s.savetofile(self.f,'lonesec.csv')
			self.s.savetofile(self.omnt.getdf(),'lonemin.csv')
			self.s.savetofile(self.fmnt.getdf(),'lfivmin.csv')
		pass
	pass





# # # # # # # # # # # # # # 
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # 


"""
 
class snap(Enum):
	brokey='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzAwNzEzMzUwLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMTE5NDk3OSJ9.y0wolqn-jA4yZGtZXuk5BEbT0xmvIRCPb5K6GXmi-4DoiLKIEeqwlSUn9RVDS525ijj-V6Glu8t5kMAYxQQIFQ'
	endpoint = "wss://nimblewebstream.lisuns.com:4576/"
	apikey = "2dd48f71-f99d-4eab-9792-b06c9aa93795"	
	brokeyy=''
class apps(Enum):
	#path = 'https://images.dhan.co/api-data/api-scrip-master.csv'
	path = 'new-oct-end.csv'
	spotprice = 19769.5
	optexpiryon = '26'
	month = 'OCT'
	year='2023'


s=scrips(snap,apps)
# futs
futgdf=s.gdflniftyfut()
print(futgdf)
futbid=s.brofutid()
print(futbid)
# calls
cesgdf=s.gdflcal()
print(cesgdf)
cesbid=s.broceid()
print(cesbid)
# puts 
cesbid=s.gdflput()
print(cesbid)
pesbid=s.bropeid()
print(pesbid)

#print(int(s.getquantity(56)))

r=rigs(s,futbid,'NIFTY-I')
r.cru_z()
r.savetofile()

"""
"""
print(s.getlotsize())
print(s.getquantity(56))
l=pd.Series([6,2,6,8,6,2,3,0,6,9,3,8,7,6,0,6,6])
print(l.apply(lambda a:a>5 and a<9))
"""


