import pandas as pd
import numpy as np
import datetime as dt
import time
import sys
from dhanhq import *
from enum import Enum
# scrips
class scrips:
	
	### time now and preset date today
	def timenow(self):
	    	return dt.datetime.now()
	    	pass
	
	def todey(self):
	    	return (dt.datetime.now()).date()
	    	pass

	### dhn operations
	def enter(self,i,k):
		try:
			d=dhanhq(i,k)
			assert(d.get_fund_limits().get('data').get('availabelBalance')>float(3000))
			print('Much more...')
		except Exception as e:
			print(f'errr: {e}')
			self.logevent(f'errr: {e}')
			sys.exit(0)
		return d
		pass
	   
	def funds(self,d):
	    	return (
			(
				d.get_fund_limits()
			).get('data')).get('availabelBalance')
	    	pass
			
	def getorderid(self,d,pos):
	    	return (
			(
				d.get_order_list()
		    	).get('data')[pos]).get('orderId')
	    	pass
	    
	def getsecurityid(self,d,pos):
	    	return (
			(
				d.get_order_list()).get('data')[pos]).get('securityId')
	    	pass
	
	def getorderstatus(self,d,pos):
	    	return (
			(
				d.get_order_list()
			).get('data')[pos]).get('orderStatus')
	
	def cancelorder(self,d,oid):
	    	return d.cancel_order(oid)
	    	pass
	
	def cancelall(self,d):
		k=d.get_order_list()
		for i in range(0, len(k.get('data'))):
			d.cancel_order(self.getorderid(d,i))
		pass
	
	# get get lot size
	def getlotsize(self):
		return self.lotsize
		pass
	
	# get quantity
	def getquantity(self,ltp):
		funds_=self.funds(self.dhn)
		return int(int((funds_/ltp)/self.getlotsize())*self.getlotsize())
		pass

	def bye(self,d,secid,q,p):
		try:
			boi = d.place_order(
				    security_id=secid,
				    exchange_segment=d.FNO,
				    transaction_type=d.BUY,
				    quantity=q,
				    order_type=d.MARKET,
				    product_type=d.INTRA,
				    price=p
				    )
		except:
			self.logevent('Error: buy order')
		finally:
			self.logevent('buy order id'+str(boi))
			return boi
		pass

	def sel(self,d,secid,q,p):
		try:
			soi = d.place_order(
				    security_id=secid,   
				    exchange_segment=d.FNO,
				    transaction_type=d.SELL,
				    quantity=q,
				    order_type=d.MARKET,
				    product_type=d.INTRA,
				    price=p
				    )
		except:
			self.logevent('Error: sell order')
		finally:
			self.logevent('buy order id'+str(soi))
			return soi
		pass
	
	### epoh conversions
	def toepoch(self,yr,mo,da,ho,mi,se):
	    	return dt.datetime(yr,mo,da,ho,mi,se).timestamp()
	    	pass
	    
	def fromepoch(self,ep):
	    	return dt.datetime.fromtimestamp(ep)
	    	pass		

	### save df to csv file
	def savetofile(self,dataframe,csvfilename):
		dataframe.to_csv(csvfilename)
		print('printing file... '+csvfilename)
		pass
		
	### event log, file read write
	def logevent(self,msg):
		try:
			with open(self.i,'a') as f:
				f.write(str(self.timenow())+" "+msg+'\n')
		except:
			print('Error: logevent file open-close')
		pass

	def readevents(self):
		try:
			with open(self.i,'r') as f:
				print(f.read())
		except:
			print('Error: readevent file open-close')
		pass
	
	def printline(self,s):
		l=''
		for i in range(0,25):
	    		l+=s
		try:
			with open(self.i, 'a') as f:
				f.write(l+'\n') #msg='Error: File open-close@ {0}'.format(dt.datetime.now()) #print(msg)
		except:
			msg='Error: printline file open-close'
			print(msg)
		pass

	# getsnaps
	def snaps(self):
	    	return self.snap
	    	pass
	
	# enum type fix
	class nest(Enum):
		me_	= '1101194979'
	
	### gdfl operations 
	def isexpiry(self): 
		return self.isexpiryday
		pass
	
	# futs
	def gdflniftyfut(self):
		return str(self.gfut)
		pass
	
	def brofutid(self):
		return str(self.futsecid)
		pass
	# calls
	def gdflcal(self):
		return str(self.gcal)
		pass
	 
	def broceid(self): 
		return str(self.ceid)
		pass
	# puts     	    
	def gdflput(self):
	    	return str(self.gput)
	    	pass
		
	def bropeid(self): 
		return str(self.peid) 
		pass

	def __init__(self, snap, apps): #
		self.snap=snap
		self.brokey=snap.brokey.value
		self.path=apps.path.value 
		self.ltp=apps.spotprice.value 
		self.optexpiryon=apps.optexpiryon.value 
		self.month=apps.month.value
		self.year=apps.year.value
		self.i='log.txt'
		self.dhn=self.enter(self.nest.me_.value,self.brokey)
		self.df=pd.read_csv(self.path)	#df.to_csv('new.csv')	# sace the new broker master list
		above=float(self.ltp+200)
		below=float(self.ltp-200)
		exdf=self.df.loc[self.df.SEM_EXM_EXCH_ID.str.contains('NSE'),:]		# get exchange
		fidf=exdf.loc[exdf.SEM_INSTRUMENT_NAME.str.contains('FUTI\w+'),:]	# get all futs id
		futarget='NIFTY '+self.month+' FUT' 					# NIFTY OCT FUT
		fudf=fidf.loc[fidf.SEM_CUSTOM_SYMBOL.str.startswith(futarget),:]
		self.futsecid=(fudf.iloc[0,2:3]).to_numpy()[0] 				# print(self.futsecid)
		oidf=exdf.loc[self.df.SEM_INSTRUMENT_NAME.str.contains('OPTI\w+'),:]	# get options id
		self.lotsize=list(oidf.SEM_LOT_UNITS)[-1]				# get lot size
		optarget='NIFTY '+self.optexpiryon+' '+self.month # NIFTY 26 OCT 19750 CALL OR, NIFTY 26 OCT #print(self.lotsize)
		tddf=oidf.loc[oidf.SEM_CUSTOM_SYMBOL.str.startswith(optarget),:] # for rows not equal to zero df[(df!=0).all(1)] # get options for given strike day
		oit=tddf.loc[tddf.SEM_STRIKE_PRICE.apply(lambda a:a<float(above) and a>float(below)),:] 
		self.ces=oit.loc[oit.SEM_OPTION_TYPE.str.contains('CE'),:]		# get all calls within the range above/below 
		self.pes=oit.loc[oit.SEM_OPTION_TYPE.str.contains('PE'),:]		# get all puts within the range above/below
 		# ceid
		def getbrocalid(strike):
			strikdf=self.ces.loc[self.ces.SEM_STRIKE_PRICE.apply(lambda a:a==strike),:]
			self.ceid=(strikdf.iloc[0,2:3]).to_numpy()[0]
			return self.ceid
			pass
		# peid
		def getbroputid(strike):
			strikdf=self.pes.loc[self.pes.SEM_STRIKE_PRICE.apply(lambda a:a==strike),:]
			self.peid=(strikdf.iloc[0,2:3]).to_numpy()[0]
			return self.peid
			pass
 		# validate in expiry is today
		if(str((dt.datetime.now()).date()) in str(list(self.pes.SEM_EXPIRY_DATE)[0])):
			self.isexpiryday=True
			self.strike_below=(int((self.ltp+50)/50)*50)-50
			self.strike_above=int((self.ltp+50)/50)*50		
			self.ceid=getbrocalid(self.strike_below)
			self.peid=getbroputid(self.strike_above)
			self.gdfce=self.strike_below
			self.gdfpe=self.strike_above
		else:
	    		self.strike_above=int((self.ltp+50)/50)*50
	    		self.strike_below=(int((self.ltp+50)/50)*50)-50
	    		self.ceid=getbrocalid(self.strike_above)
	    		self.peid=getbroputid(self.strike_below)
	    		self.gdfce= self.strike_above
	    		self.gdfpe=self.strike_below
		    	self.isexpiryday=False
		
		y = self.year[-2]+self.year[-1]
		self.gfut='NIFTY'+self.month+y+'FUT'					# NIFTY06JAN2217200CE - NIFTY 06 JAN 22 17200 FUT
		self.gcal='NIFTY'+self.optexpiryon+self.month+y+str(self.gdfce)+'CE' 	# NIFTY06JAN2217200CE - BASE+EXPDATE(2DIGIT)-MON(3CHAR)-EXPYR(2-DIGIT)-STRIKE-CE/PE				
		self.gput='NIFTY'+self.optexpiryon+self.month+y+str(self.gdfpe)+'PE'
		pass
	pass

