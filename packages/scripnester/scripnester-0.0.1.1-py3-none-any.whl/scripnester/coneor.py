#from scrinester import *
from midstral import *
from rigstral import *
from enum import Enum
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
print(s.getlotsize())
print(s.getquantity(56))
l=pd.Series([6,2,6,8,6,2,3,0,6,9,3,8,7,6,0,6,6])
print(l.apply(lambda a:a>5 and a<9))
"""


